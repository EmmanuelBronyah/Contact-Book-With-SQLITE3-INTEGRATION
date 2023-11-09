# Command-line Python Contact-book (integrated python's sqlite3 library)

The command-line python contact-book is a 
simple application which manages user 
contacts by providing features for adding,
deleting, viewing, searching and editing 
contacts from a database.

## Features of the contact-book
1. Add contact: You can add contacts by providing
contact details in the format 'name,number,address,email'.
Omitted contact details should be left blank where they will be populated
with the value None in the database. For example, omitting the address
would look like: 'name,number,,email'.
with no spaces.
2. Edit contact: You can edit contacts by providing
the name of the person whose details you want edited.
Press enter to skip the contact detail you do not want
edited, these details will maintain their 
original values and will remain unchanged in the
database.
3. View contact: You can view all contacts using
the command "view" which lists out all contacts from
the database.
4. Search contact: You can search a contact by
providing the correct name of person whose contact
you want to find.
5. Delete contact: You can delete contacts by
providing the name of the person whose contact
you want deleted.

## Getting started
1. Clone the repository to your machine 
```shell
git clone https://github.com/EmmanuelBronyah/Python-Contact-Book-With-Sqlite3-Integration.git
```

2. Navigate to project directory
```shell
cd contact-book-sqlite-integration
```

3. Run the program
```shell
python main.py
```

4. Follow the on-screen instructions to manage
your contacts.

## Usage
* When you run the code you will be prompted to
enter a command.
* Supported commands are: '"add", "view", "delete"
"edit", "search"'
* The add command requires you to input contact
details in the format 'name,number,address,email'.
Omitted contact details should be left blank where they will be populated
with the value None in the database. For example, omitting the address
would look like: 'name,number,,email'..

## Example
1. Adding contact
```shell
Enter a command > add
How many contacts do you want to add: 1
Enter contact details of contact 1 in the form "name,number,address,email": Amos,0554089278,CAPER-ST,amos@email.com
Contact saved
```

2. View contacts
```shell
Enter a command > view
1. NAME: Amos, NUMBER: 0554089278, ADDRESS: CAPER-ST, EMAIL: amos@email.com
```

3. Edit contacts
* The original value of a contact information in the
database is not modified if it is assigned no value.
The example below shows that a new address was not 
entered, therefore the value of address field of 
this contact is unchanged in the database.
```shell
Enter a command: edit
Enter the name of the person whose contact you want to edit > Amos
Enter new name: Max
Enter new number: 0234679854
Enter new address: 
Enter new email: max@email.com
```

4. Search contacts
```shell
Enter a command > search
Enter the name of the person whose contact you want to find: Max
NAME: Max
NUMBER: 0234679854
ADDRESS: CAPER-ST
EMAIL: max@email.com
```

5. Delete contacts
```shell
Enter a command > delete
Enter the name of the person whose contact you want to delete: Max
Cnntact deleted 
```

## Acknowledgement
* Built by Bronyah Emmanuel 