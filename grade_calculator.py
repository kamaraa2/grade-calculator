# Student Grade Calculator
# CST 205 - Module 1 Assignment
# Author: Abraham Kamara

# Student data: each student's name maps to a list of their grades.
student_grades = {
    "Maya": [90, 85, 78],
    "Sam": [70, 65, 80],
    "Alex": [88, 92, 79],
}

#Blank Dictionary
student_averages = {}
for name, scores in student_grades.items():
    student_averages[name] = sum(scores) / len(scores)

print(student_averages) 