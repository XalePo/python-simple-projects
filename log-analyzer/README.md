# Log Analyzer

A beginner-friendly cybersecurity project that analyzes login logs and detects suspicious IP addresses based on failed login attempts.

## Description

This program reads a log file containing login events, parses each event, counts failed login attempts by IP address, and reports any IP address with 5 or more failed attempts.

The goal of this project is to practice basic cybersecurity logic by detecting a possible brute-force login attempt.

## How It Works

The program reads data from a text file called `login_logs.txt`.

Each line in the log file contains:

```text
timestamp | username | ip_address | event | status
```
