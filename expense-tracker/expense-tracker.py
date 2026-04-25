import json
import time


def main():
    expenses = load_expenses()
    
    actions = {
        "1": display_expenses,
        "2": add_expense,
        "3": remove_expense,
        "4": display_total,
        "5": save_expenses,
    }
    
    while True:
        choice = get_user_choice(actions)

        if choice == "5":
            save_expenses(expenses)
            print("Your expenses have been saved!")
            break
        
        selected_action = actions[choice]
        selected_action(expenses)
        

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses_list_of_dicts):
    with open("expenses.json", "w") as file:
        json.dump(expenses_list_of_dicts, file)
    return


def display_expenses(expenses_list_of_dicts):
    if not expenses_list_of_dicts:
        print("You do not have any expenses at the moment.")
        time.sleep(2)
        return

    for count, dict_element in enumerate(expenses_list_of_dicts, 1):
        name = dict_element["name"]
        amount = dict_element["amount"]
        print(f"{count}. {name.capitalize()}: ${amount:.2f}")
    
    time.sleep(2.5)


def display_total(expenses_list_of_dicts):
    if not expenses_list_of_dicts:
        print("You do not have any expenses at the moment.")
        time.sleep(2)
        return
    
    total = 0
    for dict_element in expenses_list_of_dicts:
        total += dict_element["amount"]

    print(f"Total: ${total:.2f}")
    time.sleep(2)


def add_expense(expenses_list_of_dicts):
    while True:
        description = input("Enter the expense name or 0 to go back: ").strip().lower()

        if description == "0":
            return
        
        if not description:
            print("Description cannot be empty.")
            time.sleep(2)
            continue

        if not all(char.isalnum() or char.isspace() for char in description):
            print("Only letters or spaces are allowed.")
            time.sleep(2)
            continue

        break

    while True:
        try:
            cost = float(input("Enter the cost in dollars or 0 to go back: "))
        except ValueError:
            print("Only digits and decimals are allowed.")
            time.sleep(2)
            continue
        
        if cost == 0:
            return
        
        if not cost > 0:
            print("Expenses costs cannot be negative numbers.")
            time.sleep(2)
            continue
        
        break

    expenses_list_of_dicts.append({"name": description, "amount": cost})
    return


def remove_expense(expenses_list_of_dicts):
    if not expenses_list_of_dicts:
        print("You do not have expenses at the moment.")
        time.sleep(2)
        return

    while True:
        display_expenses(expenses_list_of_dicts)

        try:
            option_number = int(input("Enter the number of the expense you want to delete or enter 0 to go back: "))
        except ValueError:
            print("You need to enter a valid number.")
            time.sleep(2)
            continue
        
        if option_number == 0:
            return
        
        if not 1 <= option_number <= len(expenses_list_of_dicts):
            print("You have entered a number not associated with any expense.")
            time.sleep(2)
            continue

        del expenses_list_of_dicts[option_number - 1]
        return
    

def get_user_choice(allowed_actions):
    while True:
        user_choice = input("Use the following numbers to navigate the app: \n1 -> To display expense \n2 -> To add expense \n3 -> To remove expense \n4 -> To display the total cost \n5 -> To save and exit \nEnter number: ")
        
        if user_choice not in allowed_actions.keys():
            print("Please, you need to enter a valid number!")
            time.sleep(2)
            continue

        return user_choice


if __name__ == "__main__":
    main()