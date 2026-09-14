student_grades = {
    "Maya": [90, 85, 78],
    "Sam": [70, 65, 80],
    "Alex": [88, 92, 79],
}

grades = [90, 85, 78]
print(grades[0])
print(grades[2])    
print(len(grades))

average = sum(grades) / len(grades)
print(average)

print(round(average, 2))

for grade in grades:
    print(grade) 

for student_name, student_scores in student_grades.items():
    print(student_name, student_scores)  

print(grades)
