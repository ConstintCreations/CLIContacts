# Contacts CLI

This is a simple Python CLI Contact Book Made with Argparse

### Features

 - Add contacts by name
 - Edit Contact's name, email, or phone number
 - Delete Contacts
 - Clear Contacts
 - List Contacts

## Instalation

    pip install -i https://test.pypi.org/simple/ rw2-Constint-CLIContacts

## Usage

usage: main.py [-h] [-v] [-l] [-id ID] [-n NAME] [-e EMAIL] [-p PHONE] [-d] [-clr] [contact]

positional arguments:

  contact         |   Contact name to add

options:

  -h, --help   |      show this help message and exit <br>
  -v, --version   |   Shows version <br>
  -l, --list       |  List all contacts <br>
  -id ID           |  Specify contact ID to use <br>
  -n, --name  |  Changes a contact's name by ID <br>
  -e, --email | Adds a contact's email by ID <br>
  -p, --phone | Adds a contact's phone number by ID <br>
  -d, --delete      | Delete a contact by ID <br>
  -clr, --clear     | Clears all contacts
