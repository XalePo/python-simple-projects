# Habit Tracker

Habit Tracker is a command-line Python project that allows users to track their habits over time.

The user can add, update, remove, and display habits through the terminal. Habit progress is saved in a JSON file so the data can be loaded again in future sessions.

The project uses the `datetime` module to validate user-entered dates and the `calendar` module to display habit progress month by month. When viewing a habit, the user enters a year and month, and the program prints a calendar to the terminal. Days where the habit was completed are marked with an `X`.
