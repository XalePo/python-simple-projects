# Typing Speed Test

This is a simple command-line typing speed test built with Python.

The program chooses a random sentence from a list of sentences using the `random` module. It then asks the user to type the same sentence as accurately and quickly as possible.

After the user finishes typing, the program splits both the original sentence and the user's input into lists of words using whitespace. It then compares each typed word with the original sentence word by word, using the same index position.

The program calculates:

- Elapsed time in seconds
- Typing accuracy
- Words per minute
- Correctly typed words

The elapsed time is calculated using the `time` module. The program records the start time before the user begins typing and the end time after the user presses Enter. Then it subtracts the start time from the end time to get the total number of seconds used.

For simplicity, the sentences do not include punctuation. The program compares words directly, so capitalization matters.
