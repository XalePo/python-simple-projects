import random
import time


def main():
    word = get_random_word()
    word_chars = get_word_chars(word)
    blank_word_chars = replace_chars(word_chars)
    game_execution(word, word_chars, blank_word_chars)


def game_execution(w, w_chars, blanks):
    lives = 10
    letters_missing = len(blanks)
    guessed_letters = set()

    while lives > 0:
        print(f"{''.join(blanks)} - {letters_missing} letters missing - {lives} lives remaining")

        if letters_missing == 0:
            print(f"Congrats, you've guessed the correct word: {w}")
            break

        user_letter = get_user_letter()
        
        if user_letter in guessed_letters:
            print("You've already entered that letter! Try a new one!")
            time.sleep(2)
            continue

        guessed_letters.add(user_letter)
        
        if user_letter in w_chars:
            for index, char in enumerate(w_chars):
                if user_letter == char:
                    blanks[index] = char
                    letters_missing -= 1
        else:
            print("That letter is not in the word!")
            time.sleep(2)
            lives -= 1
    
    if lives == 0:
        print(f"I'm sorry! You've lost! The word is: {w}.")
                

def get_random_word():
    with open("/usr/share/dict/words", "r") as file:
        words = [word.strip().lower() for word in file if word.strip().isalpha()]
    return random.choice(words)


def get_word_chars(w):
    return [char for char in w]


def replace_chars(chars):
    blank_chars = []

    for _ in chars:
        blank_chars.append("_")
    return blank_chars


def get_user_letter():
    while True:
        letter = input("Enter a letter: ")
        if not (letter.isalpha() and len(letter) == 1):
            print("Please, enter only 1 valid letter!")
            time.sleep(2)
            continue
        
        return letter


if __name__ == "__main__":
    main()
