from contacts import add_contact, view_contacts, search_contact, save_to_file, load_from_file
 
def main():
    contacts = load_from_file() 

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact by name")
        print("4. Save contacts to file")
        print("5. Exit")
 
        choice = input("Choose an option (1-5): ")
 
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone_number, email)
 
        elif choice == '2':
            view_contacts(contacts)
 
        elif choice == '3':
            search_name = input("Enter name to search: ")
            search_contact(contacts, search_name)
 
        elif choice == '4':
            save_to_file(contacts)
 
        elif choice == '5':
            save_to_file(contacts) 
            print("Goodbye!")
            break
 
        else:
            print("Invalid choice. Please choose again.")
 
if __name__ == "__main__":
    main()
  