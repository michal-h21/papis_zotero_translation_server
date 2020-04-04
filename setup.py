#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0','papis','requests','logging']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Michal Hoftich",
    author_email='michal.h21@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Import bibliographic entries to Papis using Zotero Translation Server",
    entry_points={
        # 'console_scripts': [
        #     'papis_zotero_translation_server=papis_zotero_translation_server.cli:main',
        # ],
        'papis.command': [
            'zotero_translation=papis_zotero_translation_server.cli:main',
        ]
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='papis_zotero_translation_server',
    name='papis_zotero_translation_server',
    packages=find_packages(include=['papis_zotero_translation_server', 'papis_zotero_translation_server.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/michal-h21/papis_zotero_translation_server',
    version='0.1.0',
    zip_safe=False,
)
