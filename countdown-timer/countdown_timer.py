import time


def main():
    seconds = get_seconds()

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60

        print(f"Time remaining: {mins:02}:{secs:02}")
        time.sleep(1)
        seconds -= 1

    print(f"Time remaining: 00:00")
    print("Time's up!")


def get_seconds():
    while True:
        try:
            s = int(input("Enter a valid number of seconds: "))
        except ValueError:
            print("Please, enter a valid integer for seconds.")
            continue

        if s < 0:
            print("Seconds cannot be negative!")
            continue

        return s


if __name__ == "__main__":
    main()