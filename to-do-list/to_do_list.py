def main():
    tasks = load_tasks()
    choice = ""

    while choice != "4":
        choice = get_user_choice()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
    
    save_tasks(tasks)
    print("Your tasks have been saved!")


def get_user_choice():
    while True:
        user_choice = input("Enter 1 to see your tasks, 2 to add a task, 3 to delete a task or 4 to exit: ").strip()

        if user_choice not in ("1", "2", "3", "4"):
            print("Please, choose a valid option.")
            continue

        return user_choice


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = [line.rstrip() for line in file]
    except FileNotFoundError:
        return []
    
    return lines


def display_tasks(tasks_list):
    if not tasks_list:
        print("You do not have any tasks currently")
    else:
        print("These are your current tasks: ")
        for count, task_element in enumerate(tasks_list, 1):
            print(f"{count}. {task_element}")


def add_task(tasks_list):
    while True:
        new_task = input("Enter a new task: ")
        if new_task:
            tasks_list.append(new_task)
            return
        else:
            print("Field cannot be empty!")


def remove_task(tasks_list):
    if not tasks_list:
        print("You do not have any tasks.")
        return

    display_tasks(tasks_list)     
    
    while True:
        try:
            number = int(input("Enter the number for the task you wish to delete: "))
        except ValueError:
            print("Please, enter only the number for the task you wish to delete.")
            continue

        if not 1 <= number <= len(tasks_list):
            print("You entered a number that is not associated with a task!")
            continue

        del tasks_list[number - 1]

        return


def save_tasks(tasks_list):
    with open("tasks.txt", "w") as file:
        for task in tasks_list:
            file.write(task)
            file.write("\n")


if __name__ == "__main__":
    main()