import sqlite3
import textwrap


def print_intro():
    print(f'Enter "add" to add a contact \n'
          f'Enter "edit" to edit a contact \n'
          f'Enter "search" to find a contact or contacts \n'
          f'Enter "view" to view contacts \n'
          f'Enter "delete" to delete a contact \n')


def main():
    """
    Executes the entire program.

    Executes various parts of the program based on the user's input.
    Calls the create_table function which returns a connection to the database
    and a cursor object. They are assigned to the connection and cursor variables
    respectively and passed as arguments to other functions.

    """
    print_intro()

    connection, cursor = create_table()

    correct_input = True
    while correct_input:
        user_input = get_user_input()
        match user_input:
            case None:
                print('Enter a valid command')
            case 'add':
                add_contact(connection, cursor)
            case 'edit':
                edit_contact(connection, cursor)
            case 'search':
                search_contact(connection, cursor)
            case 'view':
                view_contact(connection, cursor)
            case 'delete':
                delete_contact(connection, cursor)
            case 'exit':
                correct_input = False


def create_table():
    """
    Returns a database connection and a cursor object.

    """
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    with conn:
        c.execute("""
                        CREATE TABLE Contacts (
                            name    text PRIMARY KEY NOT NULL,
                            number  text UNIQUE NOT NULL,
                            address text,
                            email   text
                        )
                     """)
    return conn, c


def get_user_input():
    """
        Takes input from the user

        Input from the user is validated against allowed inputs.
        Returns the user input if it is a verified command.
        Returns None if input from user fails validation.

        """
    allowed_inputs = ['add', 'edit', 'search', 'view', 'delete', 'exit']
    user_input = input('Enter a command > ').lower()
    if user_input in allowed_inputs:
        return user_input
    return None


def add_contact(conn, c):
    """
    Adds contacts to the Contacts table

    Contact details are received in the format 'name,number,address,email'
    where name and address cannot empty.
    Omitted contact details should be left blank where they will be populated
    with the value None in the database. For example, omitting the address
    would look like: 'name,number,,email'.

    """
    try:
        number_of_contacts = int(input('How many contacts do you want to add > '))
        if number_of_contacts > 0:
            for i in range(1, number_of_contacts + 1):
                contact = input(f'Enter contact details of contact {i} '
                                f'in the form "name,number,address,email": ').lower().split(',')
                try:
                    # cd stands for contact detail
                    contact = [None if cd == '' else cd for cd in contact]  # cd is assigned 'None' if empty
                    name, number, address, email = contact
                    with conn:
                        c.execute("INSERT INTO Contacts VALUES (:name, :number, :address, :email)",
                                  {'name': name, 'number': number, 'address': address, 'email': email})
                        print('Contact saved.')
                except ValueError:
                    text = 'Omitted fields should be left blank. ' \
                           'For example, to enter a contact with the address omitted you can enter it as: ' \
                           "Jon Carl,032566778,,joncarl@email.com"
                    if len(contact) < 4 or len(contact) > 4:
                        print(textwrap.fill(text, width=117), '\n')
                except sqlite3.IntegrityError as e:
                    match str(e).lower():
                        case 'not null constraint failed: contacts.number':
                            print('The number field cannot be empty.')
                        case 'not null constraint failed: contacts.name':
                            print('The name field cannot be empty.')
                        case 'unique constraint failed: contacts.name':
                            print('Name already exists.')
                        case 'unique constraint failed: contacts.number':
                            print('Number already exists.')
        else:
            print('Number should not be zero or less')
    except ValueError:
        print('Enter a valid number')


def edit_contact(conn, c):
    """
    Makes changes to contact details.

    The name of the person whose contact is to be edited is collected as
    input from the user.
    A contact detail of the contact to be edited maintains its original
    value if it is not assigned a new value by the user.

    """
    name = input('Enter the name of the person whose contact you want to edit: ').lower()
    with conn:
        c.execute("SELECT * FROM Contacts WHERE name = :name", {'name': name})
        contact = c.fetchone()
        if contact:
            prev_name, prev_number, prev_address, prev_email = contact
            new_name = input('Enter new name: ')
            new_number = input('Enter new number: ')
            new_address = input('Enter new address: ')
            new_email = input('Enter new email: ')
            c.execute("UPDATE Contacts SET name = :new_name, number = :new_number, address = :new_address, "
                      "email = :new_email "
                      "WHERE name = :name",
                      {'new_name': new_name if new_name != '' else prev_name,
                       'new_number': new_number if new_number != '' else prev_number,
                       'new_address': new_address if new_address != '' else prev_address,
                       'new_email': new_email if new_email != '' else prev_email,
                       'name': contact[0]})
        else:
            print('Contact does not exist.')


def view_contact(conn, c):
    """
    Lists out all the contacts in the database.

    """
    with conn:
        c.execute("SELECT * FROM Contacts")
        contacts = c.fetchall()
        if contacts:
            for index, cd in enumerate(contacts, start=1):  # cd stands for contact detail
                print(f'{index}. NAME: {cd[0]}, NUMBER: {cd[1]}, ADDRESS: {cd[2]}, EMAIL: {cd[3]}')
            print(f'Number of contacts: {len(contacts)}', '\n')
        else:
            print('Contact book is empty', '\n')


def search_contact(conn, c):
    """
    Displays the contacts information of the person whose name
    matches the name entered by the user.

    """
    name = input('Enter the name of the person whose contact you want to find: ').lower()
    with conn:
        c.execute("SELECT * FROM Contacts WHERE name = :name", {'name': name})
        contact = c.fetchone()
        if contact:
            labels = ['NAME', 'NUMBER', 'ADDRESS', 'EMAIL']
            for label, cd in zip(labels, contact):
                print(f'{label}: {cd}')
        else:
            print('There is no such contact.')


def delete_contact(conn, c):
    """
    Deletes from the database the contact whose name matches the
    name entered by the user.

    """
    with conn:
        c.execute("SELECT * FROM Contacts")
        contacts = c.fetchall()
        if contacts:
            name = input('Enter the name of the person whose contact you want to remove: ').lower()
            c.execute("SELECT * FROM Contacts WHERE name = :name", {'name': name})
            contact = c.fetchone()
            if contact:
                c.execute("DELETE FROM Contacts WHERE name = :name", {'name': contact[0]})
                print('Contact deleted.')
            else:
                print(f'Contact with contact name {name} does not exist.')
        else:
            print('Contact book is empty')


if __name__ == '__main__':
    main()
