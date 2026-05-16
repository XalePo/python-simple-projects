# System Monitor CLI

System Monitor CLI is a simple Python command-line program that displays basic system information in the terminal.

The program uses the `psutil` library to collect system data such as CPU usage, memory usage, disk usage, battery percentage, and system uptime. It then organizes that information and prints a clean report to the console.

## Features

- Shows CPU usage
- Shows memory usage
- Shows disk usage
- Shows battery percentage
- Shows system uptime
- Displays everything in a simple terminal report

## Tech Used

- Python
- psutil

## How It Works

1. The program collects system information using `psutil`.
2. The data is stored in a dictionary.
3. The dictionary is passed to a display function.
4. The program prints a formatted system report in the terminal.

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
