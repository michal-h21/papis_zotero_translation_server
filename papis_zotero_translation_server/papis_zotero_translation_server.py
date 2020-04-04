"""Main module."""
import click
import papis
import papis.bibtex
import papis.api
import papis.commands.add
import requests
import logging
import re
logger = logging.getLogger("papis:zotero-translation-server")
logger.setLevel(0)

def from_json(request):
    fields = request.json()[0] # we are interested only in the first document
    return fields

def from_bibtex(request):
    biblatex = request.text
    return papis.bibtex.bibtex_to_dict(biblatex)

def exists_in_db(fields):
    url = fields["url"] or fields.get( "URL" ) # csljson has url field in uppercase
    clean_url = re.sub(r'^.+//', "", url) # the search function has issues with : character
    # ... just hope the url doesn't contain port number
    existing = papis.api.get_documents_in_lib(search= "url:" + clean_url)
    # check if we found a document with this url
    return len(existing) > 0

def get_files(fields):
    # we may want to save files from web in the future
    # just not now
    return []


# generate alphabet list
alphabet = list(map(chr, range(97,123)))
def numbertochar(num):
    # convert number to char that can be added to the bibkey
    numletter = len(alphabet)
    charindex = num % numletter
    quotient = num / numletter
    if charindex - 1 == -1:
        charindex = numletter
        quotient = quotient - 1
    result = alphabet[charindex - 1]
    if quotient >= 1:
        return numbertochar(int(quotient)) + result
    return result

def check_bibkey(fields):
    # check for duplicate bibkeys
    bibkey = fields["ref"] or fields["id"] # csljson has bibkey in id field
    logger.info("current bibkey: " + bibkey)
    existing_bibkeys = len(papis.api.get_documents_in_lib(search= "ref:" + bibkey))
    if existing_bibkeys > 0:
        additional_letter = numbertochar(existing_bibkeys + 1)
        fields["ref"] = bibkey + additional_letter
    return fields
    
    
def process_record(fields):
    # we don't want to add duplicate entries
    if exists_in_db(fields):
        logger.error("This URL is already present in the library")
        # return -1
    files = get_files(fields)
    logger.info("Saving fields")
    logger.info(fields)
    # check for duplicate bibkeys
    fields = check_bibkey(fields)
    papis.commands.add.run([], data = fields)

def process_records(records):
    for fields in records:
        process_record(fields)

def run(url, server,format):
    logger.info("Processing URL:" + url)
    # we need to get the raw JSON data from the translators first
    r = requests.post(server + "/web", data = url, headers = {'Content-Type': 'text/plain'})
    json_data = r.text.encode("utf-8")
    # the raw JSON needs to be converted to desired data format (biblatex by default)
    data_request = requests.post(server + "/export", data = json_data, headers = {'Content-Type': 'application/json'}, params = {'format':format})
    # check if the format is supported
    if format=="biblatex" or format=="bibtex":
        records = from_bibtex(data_request)
    elif format=="csljson":
        records = from_json(data_request)
    else:
        logger.error("Unsupported format: " + format)
        return -1
    if records == None:
        logger.error("Error in parsing")
        return -1
    # process records
    process_records(records)






