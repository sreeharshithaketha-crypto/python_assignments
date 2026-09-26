# Mini Project 1: Simple student management system.
class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

students = {}

def add_student(student):
    students[student.roll] = student

def search_student(roll):
    return students.get(roll)

def delete_student(roll):
    students.pop(roll, None)

add_student(Student(1, "Asha"))
add_student(Student(2, "Ravi"))
print(search_student(1).name)
students[1].name = "Anu"
delete_student(2)
print([student.name for student in students.values()])
