import random


def main():
    upper_bound = 100
    lower_bound = 0
    attempts = 0

    print("Think of a number!")

    while True:
        if lower_bound > upper_bound:
            print("Your answers were inconsistent!")
            break

        computer_number = random.randint(lower_bound, upper_bound)
        print(computer_number)

        feedback = input("Was it too high, too low or correct? ").lower().strip()

        if feedback in ("correct", "yes"):
            if attempts > 3:
                print("It took me a while!")
            elif attempts > 0:
                print("I got it!")
            else:
                print("I knew it!")
            break

        elif feedback == "too low":
            lower_bound = computer_number + 1
            attempts += 1
            
        elif feedback == "too high":
            upper_bound = computer_number - 1
            attempts += 1
            
        else:
            print("Please enter: too high, too low, or correct.")


if __name__ == "__main__":
    main()