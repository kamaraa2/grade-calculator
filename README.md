# Student Grade Calculator

A Python program that calculates and analyzes student grades for a single course.
It stores each student's grades, calculates their average, assigns a letter grade,
identifies the top performer, and reports class-wide statistics.

Built for CST 205 Module 1.

## Features

- Stores student names and their grades in a dictionary
- Calculates each student's average grade
- Assigns letter grades (A-F) using a standard grading scale
- Identifies the top performing student and their average
- Calculates the overall class average
- Counts how many students received a passing grade (C or better)

## How to Run

Requires Python 3.

```bash
python3 grade_calculator.py
```

## Example Output

```
Student Averages:
Maya: 84.33
Sam: 71.67
Alex: 86.33
{'Maya': 'B', 'Sam': 'C', 'Alex': 'B'}
Top Performer is Alex! with an average of 86.33!!!
The class average is: 80.78
Passing count for the amount of students who passed is: 3
```

## How It Works

I used a dictionary to store the data, where each student's name is the key and a list
of their grades is the value. A dictionary made sense here because each student needs to
be looked up by name rather than by position, and a list works as the value because every
student has more than one grade.

To get from grades to letters, I loop through each student's average and use an
if/elif/else chain to put it into the right letter range. The order matters because Python
stops at the first condition that is true, so the highest threshold has to be checked
first — otherwise every score would fall into the lowest one.

To find the top performer, I keep track of the highest average I have seen so far and
compare each student against it as I loop through. If a student's average is higher, they
become the new top performer. Counting how many students passed works the same way, using
a counter that goes up by one each time a letter grade is A, B, or C.

## Screencast

https://www.loom.com/share/7bdf79344afc40eaaf8ca00aded4e52a

## Author

Abraham Kamara
CST 205 — Introduction to Programming with Python
Module 1 Assignment
