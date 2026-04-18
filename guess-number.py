import random


def main():
    number = random.randint(0, 100)

    while True:
        try:
            user_number = int(input("Enter a number between 0 and 100: "))
        except ValueError:
            print("Please, enter a valid integer!")
            continue

        if user_number < 0:
            print("Please, enter a non-negative number!")
            continue
        
        if user_number == number:
            print("Congrats, you've guessed the number!")
            return
        elif user_number > number:
            print("Too large!")
        else:
            print("Too small!")

if __name__ == "__main__":
    main()
