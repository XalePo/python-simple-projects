# Contact Book

## Description

Contact Book is a command-line Python program that allows users to manage a simple list of contacts. The user can add, display, search, edit, and remove contacts. The program also saves the contact list into a JSON file so the data remains available after the program closes.

This project was built to practice Python fundamentals such as functions, loops, dictionaries, lists, JSON file handling, input validation, and basic command-line interface design.

## Features

- Display all saved contacts
- Add a new contact
- Search for a contact by full name
- Edit an existing contact
- Remove a contact
- Save contacts to a JSON file
- Load contacts from a JSON file
- Validate phone numbers
- Format phone numbers for display

## Technologies Used

- Python
- JSON module
- Time module
- Command-line interface

## Data Storage

Contacts are stored in a JSON file using a list of dictionaries.

Example:

```json
[
  {
    "name": "john doe",
    "phone": "5551234567"
  },
  {
    "name": "jane doe",
    "phone": "5559876543"
  }
]
```
