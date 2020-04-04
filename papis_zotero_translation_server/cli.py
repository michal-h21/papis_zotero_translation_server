"""Console script for papis_zotero_translation_server."""
import sys
import click
import papis_zotero_translation_server
import papis.config

options = {
    'settings': {
        'translation-server' : 'http://127.0.0.1:1969',
        'translation-format' : 'biblatex'
    }
}
papis.config.register_default_settings(options)


@click.command()
@click.help_option('--help', '-h')
@click.argument("url")
@click.option("--format", "-f",
    help="Format that will be imported to Papis. biblatex by default",
    type=str,
    default=papis.config.get('translation-format')
)
@click.option("--library","-l",
    help="Select Papis library",
    type=str
)
@click.option("--server", "-s",
    help="Address of the Zotero Translation Server",
    type=str,
    default=papis.config.get('translation-server')
)
def main(url, server, format,library):
    """Console script for papis_zotero_translation_server."""
    # select the library if we don't want to use the default 
    if library:
        papis.config.set_lib_from_name(library)
    papis_zotero_translation_server.run(url,server, format)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
