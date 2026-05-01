import json
import time


def main():
    contact_book = load_contacts()

    actions = {
        "1": search_contact, 
        "2": add_contact,
        "3": edit_contact,
        "4": remove_contact,
        "5": display_all_contacts,
        "6": save_contacts,
    }

    while True:
        choice = get_user_choice(actions)

        if choice == "6":
            selected_choice = actions[choice]
            selected_choice(contact_book)
            print("You've exited the program.")
            break

        selected_choice = actions[choice]
        selected_choice(contact_book)


def load_contacts():
    try:
        with open("contact-book.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def display_all_contacts(contacts):
    if not contacts:
        print("There are no contacts to display. The book is empty.")
        time.sleep(2)
        return
    
    for count, contact in enumerate(contacts, 1):
        name = contact["name"]
        phone = contact["phone"]
        first = phone[:3]
        middle = phone[3:6]
        last = phone[6:]
        print(f"{count}. {name.title()}: ({first}) {middle}-{last}")
    time.sleep(2)


def save_contacts(contacts):
    with open("contact-book.json", "w") as f:
        json.dump(contacts, f)
    return


def add_contact(contacts):
    contact_info = validate_contact()

    if contact_info is None:
        return
    
    name, phone = contact_info
    contacts.append({"name": name, "phone": phone})
    return


def validate_contact():
    while True:
        contact_name = input("Enter the contact's full name or 0 to cancel: ").strip().lower()

        if contact_name == "0":
            return

        if not contact_name:
            print("Name cannot be empty.")
            time.sleep(2)
            continue

        if not all(char.isalpha() or char.isspace() for char in contact_name):
            print("Names can only contain alphabet letters and spaces.")
            time.sleep(2)
            continue
            
        break

    while True:
        contact_phone = input("Enter the US contact's phone number without the country code or 0 to cancel: ")

        if contact_phone == "0":
            return
        
        if not all(char.isnumeric() for char in contact_phone):
            print("Phone numbers can only contain digits.")
            time.sleep(2)
            continue

        if not len(contact_phone) == 10:
            print("US phone numbers have 10 digits without the country code.")
            time.sleep(2)
            continue

        break
        
    return (contact_name, contact_phone)


def remove_contact(contacts):
    if not contacts:
        print("There are no contacts to display. The book is empty.")
        time.sleep(2)
        return
    
    while True:
        contact_to_del = input("Enter contact's full name to delete or 0 to cancel: ").strip().lower()

        if contact_to_del == "0":
            return
        
        for index, contact in enumerate(contacts):
            
            if contact["name"] == contact_to_del:
                del contacts[index]
                print("Contact has been deleted successfully!")
                time.sleep(2)
                return
        
        print("Contact not found!")
        time.sleep(2)
        return
    

def edit_contact(contacts):
    if not contacts:
        print("There are no contacts to display. The book is empty.")
        time.sleep(2)
        return
    
    while True:
        contact_to_edit = input("Enter the contact's full name you want to edit or 0 to cancel: ").strip().lower()

        if contact_to_edit == "0":
            return

        for contact in contacts:
            if contact["name"] == contact_to_edit:
                print("Follow the steps to edit the contact: ")
                time.sleep(2.5)

                contact_info = validate_contact()

                if contact_info is None:
                    return
                
                new_name, new_phone = contact_info

                contact["name"] = new_name
                contact["phone"] = new_phone
                
                return
        
        print("Contact not found. Please, make sure it matches exactly!")
        time.sleep(2)
        return
     

def search_contact(contacts):
    if not contacts:
        print("There are no contacts to display. The book is empty.")
        time.sleep(2)
        return
    
    while True:
        contact_to_search = input("Enter contact's full name to search or 0 to cancel: ").strip().lower()

        if contact_to_search == "0":
            return
        
        for contact in contacts:
            
            if contact["name"] == contact_to_search:
                name = contact["name"]
                phone = contact["phone"]
                first = phone[:3]
                middle = phone[3:6]
                last = phone[6:]
                print(f"Contact found: {name.title()}: ({first}) {middle}-{last}")
                time.sleep(2.5) 

                return

        print("Contact not found!")
        time.sleep(2)
        return
        
        
def get_user_choice(actions):
    while True:
        user_choice = input("Enter the number associated to the action to execute it: \n1 -> Search \n2 -> Add \n3 -> Edit \n4 -> Delete \n5 -> Display all \n6-> Exit \nEnter number: ")

        if user_choice not in actions.keys():
            print("You've entered a number not associated with any action! Try again!")
            time.sleep(2)
            continue

        return user_choice


if __name__ == "__main__":
    main()