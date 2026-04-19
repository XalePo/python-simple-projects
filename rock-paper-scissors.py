import random 


def main():
    options = ["rock", "paper", "scissors"]
    play_again = True

    while play_again:
        user = input(f"Make your choice: rock, paper or scissors? ").lower().strip()
        computer = random.choice(options)

        print(f"Computer chose: {computer}")

        if user == computer:
            print("Tie!")
        elif user == "rock" and computer == "scissors":
            print("You win!")
        elif user == "paper" and computer == "rock":
            print("You win")
        elif user == "scissors" and computer == "paper":
            print("You win")
        elif user in options:
            print("You lose!")
        else:
            print("Please enter rock, paper or scissors.")
        
        play_again = ask_to_play_again()
        

def ask_to_play_again():
    response = input("Want to play again? Yes or No? ").lower().strip()

    if response == "no":
        print("It was a pleasure! Take care!")
        return False
    
    return True
        

if __name__ == "__main__":
    main()