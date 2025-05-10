# Phone Book Application

def add_contact(phonebook):
    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")

    if name in phonebook:
        print(f"Contact {name} already exists. Updating phone number.")
    else:
        print(f"Contact {name} added successfully to the phonebook.")

    phonebook[name] = phone  # Add or update
    


def search_contact(phonebook):
    name = input("Enter Contact Name to Search: ")

    if name in phonebook:
        print(f"Contact {name} found with phone number: {phonebook[name]}")
    else:
        print(f"Contact {name} not found in the phonebook.")


def delete_contact(phonebook):
    name = input("Enter Contact Name to Delete: ")

    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully from the phonebook.")
    else:
        print(f"Contact {name} not found in the phonebook.")


def display_contacts(phonebook):
    if phonebook:
        print("Phone Book Contacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phone book is empty. No contacts to display.")


if __name__ == "__main__":
    phonebook = {}

    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            delete_contact(phonebook)
        elif choice == '4':
            display_contacts(phonebook)
        elif choice == '5':
            print("Exiting Phone Book.")
            break
        else:
            print("Invalid choice. Please try again.")
