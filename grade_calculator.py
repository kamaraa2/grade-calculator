# Student Grade Calculator
# CST 205 - Module 1 Assignment
# Author: Abraham Kamara


student_grades = {
    "Maya": [90, 85, 78],
    "Sam": [70, 65, 80],
    "Alex": [88, 92, 79],
}

student_averages = {}
for name, scores in student_grades.items():
    student_averages[name] = sum(scores) / len(scores)

print(student_averages) 

student_letter_grades = {}

for name, average in student_averages.items():
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    student_letter_grades[name] = letter

print(student_letter_grades)

top_name = ""
top_average = 0

for name, average in student_averages.items():
    if average > top_average:
        top_average = average
        top_name = name 

print(f"Top Performer is {top_name}! with an average of {top_average}!!!")

class_average = sum(student_averages.values()) / len(student_averages)

passing_count = 0

for letter in student_letter_grades.values():
    if letter in ["A", "B", "C"]:
        passing_count += 1

print(f"The class average is: {class_average}")
print(f"Passing count for the amount of students who passed is: {passing_count}")
