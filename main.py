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

parser.add_argument("-v", "--version", help="Shows version", action="version", version="0.0.1")
parser.add_argument("-l", "--list", help="List all contacts", action="store_true")
parser.add_argument("-id", type=int, help="Specify contact ID to use")
parser.add_argument("-n", "--name", type=str, help="Changes a contact's name by ID")
parser.add_argument("-e", "--email", type=str, help="Adds a contact's email by ID")
parser.add_argument("-p", "--phone", type=str, help="Adds a contact's phone number by ID")
parser.add_argument("-d", "--delete", help="Delete a contact by ID", action="store_true")
parser.add_argument("-clr", "--clear", help="Clears all contacts", action="store_true")
parser.add_argument("contact", type=str, nargs="?", help="Contact name to add")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.list:
    contacts = load_contacts()
    if len(contacts) == 0:
        print("No contacts were found")
    else:
        for contact in contacts:
            email = f"Email: {contact['email']}" if contact['email'] else ""
            phone = f"Phone Number: {contact['phone']}" if contact['phone'] else ""
            print(f"{contact['id']}: {contact['contact']} {"-" if contact['email'] or contact['phone'] else ""} {email}{" | " if contact['email'] and contact['phone'] else ""}{phone}")
    sys.exit(0)

elif args.id:
    contacts = load_contacts()
    found_contact = False
    for contact in contacts:
        if contact["id"] == args.id:
            found_contact = True

            if args.delete:
                contacts.remove(contact)
                save_contacts(contacts)
                print(f"Contact with ID of {args.id} deleted")
                sys.exit(0)

            if args.name:
                contact['contact'] = args.name
                save_contacts(contacts)
                print(f"Name Changed to {args.name}")

            if args.email:
                contact['email'] = args.email
                save_contacts(contacts)
                print(f"Email Changed to {args.email}")

            if args.phone:
                contact['phone'] = args.phone
                save_contacts(contacts)
                print(f"Phone Number Changed to {args.phone}")

        email = f"Email: {contact['email']}" if contact['email'] else ""
        phone = f"Phone Number: {contact['phone']}" if contact['phone'] else ""

        print(f"Contact at ID {args.id}:")
        print(f"{contact['id']}: {contact['contact']} {"-" if contact['email'] or contact['phone'] else ""} {email}{" | " if contact['email'] and contact['phone'] else ""}{phone}")    

    if not found_contact:
        print(f"Contact with ID of {args.id} could not be found")

elif args.clear:
    contacts = []
    save_contacts(contacts)
    print(f"All contacts have been cleared")
elif args.contact:
    contacts = load_contacts()
    if len(contacts) == 0:
        new_id = 1
    else:
        new_id = contacts[-1]["id"] + 1
    contacts.append({"id": new_id, "contact": args.contact, "email": None, "phone": None})
    save_contacts(contacts)

    print(f"Contact with Name {args.contact} added with ID of {new_id}")