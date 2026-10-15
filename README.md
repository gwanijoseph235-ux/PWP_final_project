# TutorTrack GradeBook

TutorTrack GradeBook is a simple Python-based student grade management system. It allows you to record student scores, view student summaries, and analyze subject performance across the class.

## Project Overview

This project stores records in a text file named `gradebook.txt` and uses a nested dictionary structure to manage data in memory. It demonstrates core Python concepts such as:

- Variables and data types
- Operators
- Conditional statements
- Loops
- Functions
- Dictionaries
- String handling
- File reading and writing
- Error handling with `try/except`

## Features

- Add or update a student score
- View each student's subject marks and average
- View subject analytics and identify the top performer in each subject
- Save records automatically to a file
- Reload saved data when the program starts

## Files in This Project

- `main.py` — contains the application logic and menu interface
- `gradebook.txt` — stores the saved gradebook data
- `README.md` — project documentation

## How to Run

1. Open the project folder.
2. Make sure Python is installed on your computer.
3. Run the program using:

```bash
python main.py
```

## Example Menu Options

1. Record / Update Student Score
2. View Student Grade Summaries
3. View Subject Analytics & Top Performers
4. Exit

## Data Format

The gradebook data is stored in this format:

```text
StudentName|Subject|Score
```

Example:

```text
Alex Johnson|Mathematics|88.5
Fatima Ali|Physics|85.0
```

## Notes

- Scores must be between 0 and 100.
- Blank lines in the data file are ignored.
- If the gradebook file does not exist yet, the program creates it automatically when saving.

## Author

This is a final project gradebook application built for learning Python programming fundamentals.
