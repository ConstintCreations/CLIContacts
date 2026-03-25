import argparse
import sys
import os
import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)
    
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file,indent=4)

parser = argparse.ArgumentParser()
parser.add_argument("contact", type=str, nargs="?", help="Contact name to add")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.contact:
    contacts = load_contacts()
    if len(contacts) == 0:
        new_id = 1
    else:
        new_id = contacts[-1]["id"] + 1
    contacts.append({"id": new_id, "contact": args.contact})
    save_contacts(contacts)

    print(f"Contact with Name {args.contact} added with ID of {new_id}")