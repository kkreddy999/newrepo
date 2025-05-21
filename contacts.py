import csv
 
def add_contact(contacts, name, phone_number, email):
    contacts.append({'name': name, 'phone_number': phone_number, 'email': email})
 
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
 
def search_contact(contacts, search_name):
    found = False
    for contact in contacts:
        if search_name.lower() in contact['name'].lower():
            print(f"Found - Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print("No contact found with that name.")
 

def save_to_file(contacts):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone_number", "email"])  
        for contact in contacts:
            writer.writerow([contact['name'], contact['phone_number'], contact['email']]) 
    print("Contacts saved to file.")
 
def load_from_file():
    contacts = []
    try:
        with open("contacts.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                contacts.append({'name': row[0], 'phone_number': row[1], 'email': row[2]})
    except FileNotFoundError:
        print("No file found. Starting with an empty contact list.")
    return contacts