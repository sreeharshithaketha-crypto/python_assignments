# 1. Create two sets of student names and use a dictionary to store each student's course.
python_students = {"Asha", "Ravi"}
java_students = {"Neha", "Amit"}
courses = {}
for student in python_students:
    courses[student] = "Python"
for student in java_students:
    courses[student] = "Java"
print(courses)
