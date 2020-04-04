===============================
Papis Zotero Translation Server
===============================


.. image:: https://img.shields.io/pypi/v/papis_zotero_translation_server.svg
        :target: https://pypi.python.org/pypi/papis_zotero_translation_server

.. image:: https://img.shields.io/travis/michal-h21/papis_zotero_translation_server.svg
        :target: https://travis-ci.com/michal-h21/papis_zotero_translation_server

.. image:: https://readthedocs.org/projects/papis-zotero-translation-server/badge/?version=latest
        :target: https://papis-zotero-translation-server.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Import bibliographic entries to Papis using Zotero Translation Server"


* Free software: MIT license
* Documentation: https://papis-zotero-translation-server.readthedocs.io.


Introduction
------------

`Papis <https://github.com/papis/papis>`_ is a command line bibliography
manager. This project adds support for `Zotero Translation Server
<https://github.com/zotero/translation-server>`_, which can be used to import
bibliographic information from web pages supported by Zotero translators.

There is already `support <https://github.com/papis/papis-zotero>`_ for Zotero
translators in Papis, but the imported data are in the Zotero's internal
format, which is not easy to convert to something supported target
applications, such as BibLaTeX, BibTeX or Citeproc. After some experiments,
I've decided to use the Zotero Translation Server. It already supports
conversion to various data models, so we can select the most suitable one
according to the desired use. 

Usage
-----

::

  papis zotero_translation [options] URL

The required argument is URL address with bibliographic information you want to
import. Without options, it will import data in the BibLaTeX format. BibLaTeX
is successor of BibTeX with much higher number of supported publication types
and supported fields.

Supported options:

-h, --help          Show this message and exit.
-f, --format TEXT   Format that will be imported to Papis. biblatex by
                    default
-l, --library TEXT  Select Papis library
-s, --server TEXT   Address of the Zotero Translation Server

Supported formats:

- biblatex
- bibtex
- csljson

Default address of the server is ``http://127.0.0.1:1969``.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
