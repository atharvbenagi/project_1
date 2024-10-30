import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file if exists
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

# Function to create a contact
def create_contact(name, phone):
    if name in contacts:
        print(f"Contact '{name}' already exists.")
    else:
        contacts[name] = phone
        save_contacts()
        print(f"Contact '{name}' added successfully.")

# Function to read/display all contacts
def read_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

# Function to update a contact
def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        save_contacts()
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

# Load contacts when program starts
contacts = load_contacts()

# Main program loop
while True:
    print("\nContact Book")
    print("1. Create Contact")
    print("2. Read Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        create_contact(name, phone)

    elif choice == '2':
        read_contacts()

    elif choice == '3':
        name = input("Enter the name of the contact to update: ")
        phone = input("Enter the new phone number: ")
        update_contact(name, phone)

    elif choice == '4':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)

    elif choice == '5':
        name = input("Enter the name of the contact to search: ")
        search_contact(name)

    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
