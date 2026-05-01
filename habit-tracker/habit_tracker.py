import json
import time
import calendar as c
import datetime as dt
from datetime import date


def main():
    habits = load_habits()

    actions = {
        "1": display_habit,
        "2": update_habit,
        "3": add_habit,
        "4": remove_habit,
        "5": display_all_habits,
        "6": save_habits,
    }

    while True:
        choice = get_choice(actions)

        if choice == "6":
            save_habits(habits)
            print("You've exited the program")
            break
        else:
            selected_choice = actions[choice]
            selected_choice(habits)


def load_habits():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("habits.json", "w") as f:
            json.dump({}, f)
        return {}
    except json.JSONDecodeError:
        with open("habits.json", "w") as f:
            json.dump({}, f)
        return {}


def display_all_habits(habs):
    if no_habit_present(habs):
        return
    
    for count, habit in enumerate(habs.keys(), 1):
        print(f"{count}. {habit.title()}")
    time.sleep(2.5)


def display_habit(habs):
    if no_habit_present(habs):
        return 
    
    hab_to_display = is_hab_present(habs)
    year, month = get_year_month()
 
    cal = c.TextCalendar()
    weeks = cal.monthdayscalendar(year, month)

    print(c.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    for week in weeks:
        for day in week:
            if day == 0:
                print(" ", end=" ")
                continue

            date_str = f"{month:02d}-{day:02d}-{year}"

            if date_str in habs[hab_to_display]:
                print("X", end=" ")
            else:
                print(f"{day:2}", end=" ")

        print()
    time.sleep(3)


def update_habit(habs):
    if no_habit_present(habs):
        return

    hab_to_update = is_hab_present(habs)

    print("Enter all the days you did the habit one by one in format \"MM-DD-YYYY\".\nPress 0 to stop entering dates.")
    while True:
        hab_date = input("-> ")

        if hab_date == "0":
            return

        if len(hab_date) != 10:
            print("Use \"MM-DD-YYYY\"")
            continue

        try:
            valid_date = dt.datetime.strptime(hab_date, "%m-%d-%Y")
        except ValueError:
            print("Invalid date format.")
            time.sleep(2)
            continue

        formatted_date = valid_date.strftime("%m-%d-%Y")
        habs[hab_to_update].append(formatted_date)

    
def add_habit(habs) -> None:
    new_habit_str = get_habit()

    while True:
        did_today = input("Did you do the new habit today (Yes/No)?\n-> ").strip().lower()

        if did_today not in ("yes", "no"):
            print("Only \"Yes\" or \"No\" are allowed!")
            time.sleep(2)
            continue
        if did_today == "yes":
            today = date.today()
            formatted_today = today.strftime("%m-%d-%Y")
            new_habit = {new_habit_str : [formatted_today]}
            habs.update(new_habit)
            return
        else:
            new_habit = {new_habit_str : []}
            habs.update(new_habit)
            return


def remove_habit(habs):
    if no_habit_present(habs):
        return

    hab_to_del = is_hab_present(habs)

    del habs[hab_to_del]
    print("Habit has been deleted!")


def save_habits(habs):
    with open("habits.json", "w") as f:
        json.dump(habs, f)


def get_choice(actions):
    while True:
        user_choice = input("Enter the number associated to the instruction:\n1 -> Display Habit Progress\n2 -> Update Habit Progress\n3 -> Add New Habit\n4 -> Delete Habit\n5 -> Display All Habits\n6 -> Exit\nEnter number: ")

        if user_choice not in actions.keys():
            print("You have enter a number not associated with any action! Try again!")
            time.sleep(2)
            continue

        return user_choice
    

def get_habit():
    while True:
        user_habit = input("Enter a habit: ").strip().lower()

        if not user_habit:
            print("Habit cannot be empty.")
            time.sleep(2)
            continue

        if not all(char.isalnum() or char.isspace() for char in user_habit):
            print("Habits can only contain letters, numbers or spaces.")
            time.sleep(2)
            continue

        return user_habit
    

def is_hab_present(habs):
    while True:
        habit = input("Please, enter habit: ").strip().lower()

        if habit not in habs.keys():
            print("Habit not found! Make sure it matches!")
            time.sleep(2)
            continue

        return habit
    

def get_year_month():
    while True:
        year = input("Enter the year: ")

        if len(year) != 4:
            print("Use a 4-digit year.")
            time.sleep(2)
            continue

        try:
            year = int(year)
        except ValueError:
            print("Use a 4-digit year.")
            time.sleep(2)
            continue

        try:
            month = int(input("Enter the month as a number: "))
        except ValueError:
            print("Enter the month as a number")
            time.sleep(2)
            continue

        if not 1 <= month <= 12:
            print("Month does not exist. Make sure it is between 1 and 12.")
            time.sleep(2)
            continue
            
        return (year, month)
    

def no_habit_present(habs):
    if not habs:
        print("There are not habits present.")
        time.sleep(2)
        return True
    return False
    

if __name__ == "__main__":
    main()