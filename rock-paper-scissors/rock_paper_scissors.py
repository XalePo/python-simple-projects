import random 


def main():
    options = ["rock", "paper", "scissors"]
    play_again = True
    user_score = 0
    computer_score = 0

    while play_again:
        user = input(f"Make your choice: rock, paper or scissors? ").lower().strip()
        computer = random.choice(options)

        print(f"Computer chose: {computer}")

        if user == computer:
            print("Tie!")
        elif user == "rock" and computer == "scissors":
            print("You win!")
            user_score += 1
        elif user == "paper" and computer == "rock":
            print("You win")
            user_score += 1
        elif user == "scissors" and computer == "paper":
            print("You win")
            user_score += 1
        elif user in options:
            print("You lose!")
            computer_score += 1
        else:
            print("Please enter rock, paper or scissors.")
        
        print(f"User score: {user_score} - Computer score: {computer_score}")
        
        play_again = ask_to_play_again()
        

def ask_to_play_again():
    response = input("Want to play again? Yes or No? ").lower().strip()

    if response == "no":
        print("It was a pleasure! Take care!")
        return False
    
    return True
        

if __name__ == "__main__":
    main()