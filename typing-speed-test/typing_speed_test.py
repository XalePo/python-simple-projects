from typing import List
import random
import time


def main():
    random_sentence = get_random_sentence()

    print(f"Welcome to the Typing Speed Test!\nType the following sentence:\n{random_sentence}")

    split_random_sentence = random_sentence.split()

    start_time = get_time()
    user_input = get_user_input()
    end_time = get_time()

    elapsed_time = end_time - start_time
    accuracy = calc_accuracy(split_random_sentence, user_input)
    wpm = calc_wpm(user_input, elapsed_time)

    print(f"Results:\nAccuracy: {accuracy:.2f}%\nWords per minute: {wpm:.2f}\nTime taken: {elapsed_time:.1f} seconds.")

def get_random_sentence() -> str:
    sentences = [
        "Let us take this offline",
        "Could you please repeat that",
        "The silence was as deep as the oceans abyss",
        "On my way",
        "I will follow up by email",
        "I see what you are saying",
        "The city was a canvas of stories",
        "Practice makes progress over time",
        "Python is fun when you understand it",
        "Small steps lead to big results",
        "The sun rises over the quiet hills",
        "Learning to code takes patience",
        "Clear thinking makes better programs",
        "Typing fast requires focus and rhythm"
    ]
    
    return random.choice(sentences)
    

def get_user_input() -> List["str"]:
    return input("Start typing:\n").split()


def calc_wpm(u_input, elapsed_t):
    return len(u_input) / (elapsed_t / 60)


def calc_accuracy(r_sentence: List["str"], u_input: List["str"]) -> float:
    total = len(r_sentence)
    correct = 0

    for i in range(min(len(r_sentence), len(u_input))):
        if r_sentence[i] == u_input[i]:
            correct += 1

    return (correct / total) * 100


def get_time():
    return time.time()


if __name__ == "__main__":
    main()