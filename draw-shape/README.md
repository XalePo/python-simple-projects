# Draw Shape

Draw Shape is a simple Python program that uses Pygame to display animated ASCII art shapes on the screen.

The program stores a dictionary of ASCII shapes, randomly selects one when the program starts, converts the shape into screen coordinates, shuffles those coordinates, and then draws the shape little by little using animated particles/lines.

## Features

- Opens a Pygame window
- Uses a black background
- Randomly selects a shape from an internal ASCII dictionary
- Converts ASCII art characters into screen coordinates
- Uses the `random` module to shuffle the drawing order
- Animates the shape by revealing points gradually
- Uses Pygame to draw the shape on the screen

## How It Works

The program starts by selecting one random shape from a dictionary of ASCII art patterns.

Each shape is stored as a list of strings. Every non-space character is treated as part of the shape. The program scans each row and column of the ASCII art and converts those positions into screen coordinates.

After all coordinates are collected, the program shuffles them using the `random` module. This allows the shape to appear in a random order instead of being drawn from left to right.

Pygame then draws the shape gradually on a black screen until the full ASCII form is completed.

## Technologies Used

- Python
- Pygame
- Random module

## Project Purpose

This project was created to practice beginner Python and Pygame concepts, including:

- Working with loops
- Using dictionaries
- Using lists
- Reading and converting coordinate positions
- Drawing to a Pygame window
- Creating a basic animation loop
- Organizing simple game logic

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
