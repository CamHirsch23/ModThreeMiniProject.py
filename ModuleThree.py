import json

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact(contacts):
    email = input("Enter contact's email: ")
    if email in contacts:
        print("Contact already exists.")
    else:
        name = input("Enter contact's name: ")
        phone = input("Enter contact's phone number: ")
        additional_info = input("Enter additional information: ")
        contacts[email] = {
            "name": name,
            "phone": phone,
            "additional_info": additional_info
        }
        print("Contact added.")

def edit_contact(contacts):
    email = input("Enter the email of the contact to edit: ")
    if email in contacts:
        name = input("Enter new name (leave blank to keep current): ")
        phone = input("Enter new phone number (leave blank to keep current): ")
        additional_info = input("Enter new additional information (leave blank to keep current): ")
        if name:
            contacts[email]['name'] = name
        if phone:
            contacts[email]['phone'] = phone
        if additional_info:
            contacts[email]['additional_info'] = additional_info
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    email = input("Enter the email of the contact to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    email = input("Enter the email of the contact to search for: ")
    if email in contacts:
        contact = contacts[email]
        print("Contact details:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Additional Information: {contact['additional_info']}")
    else:
        print("Contact not found.")

def display_all_contacts(contacts):
    if contacts:
        for email, info in contacts.items():
            print(f"\nEmail: {email}")
            print(f"Name: {info['name']}")
            print(f"Phone: {info['phone']}")
            print(f"Additional Information: {info['additional_info']}")
    else:
        print("No contacts to display.")

def export_contacts(contacts):
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)
    print("Contacts exported successfully.")

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = json.load(file)
        print("Contacts imported successfully.")
        return contacts
    except FileNotFoundError:
        print("No file found.")
        return {}

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            edit_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            display_all_contacts(contacts)
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            contacts = import_contacts()
        elif choice == "8":
            print("Thank you for using the Contact Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
