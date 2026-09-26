# Q1: Create three Student objects with instance variables.
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

students = [Student("Asha", 18, "BCA"), Student("Ravi", 19, "BBA"), Student("Mina", 18, "BSc")]
for student in students:
    print(student.name, student.age, student.course)
