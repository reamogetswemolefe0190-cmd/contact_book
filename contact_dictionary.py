def add_contact(contact_list):
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')

    new_contact = {'name': name, 'phone': phone, 'email': email}
    contact_list.append(new_contact)

contacts = []

add_contact(contacts)
print(contacts)

#for searching for contacts
def search_contact(contact_list, name):
    for contact in contact_list:
        if contact['name'] == name:
            return contact
    return None

#for deleting contacts
def delete_contact(contact_list, name):
    contact_to_delete = search_contact(contact_list, name)

    if contact_to_delete is not None:
        contact_list.remove(contact_to_delete)
        print(f'{name} has been deleted.')
    else:
        print(f'{name} not found.')

#view all function
def view_all(contact_list):
    if len(contact_list) == 0:
        print('No contacts saved yet.')
    else:
        print('\n--- All Contacts ---')
        for contact in contact_list:
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
        print('---------------------------\n')

    
#while loop menu to let the user choose an action
contacts = []

while True:
    print('\n1. Add Contact')
    print('2. Search Contact')
    print('3. Delete Contact')
    print('4. View All Contacts')
    print('5. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        add_contact(contacts)

    elif choice == '2':
        name = input('Enter name to search: ')
        result = search_contact(contacts, name)
        if result is not None:
            print(result)
        else:
            print(f'{name} not found.')

    elif choice =='3':
        name = input('Enter name to delete: ')
        delete_contact(contacts, name)

    elif choice == '4':
        view_all(contacts)

    elif choice == '4':
        print('Goodbye!')
        break

    else:
        print('Invalid option, try again.')
