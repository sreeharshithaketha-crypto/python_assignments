# Q1: Demonstrate the difference between class and instance variables.
class Student:
    school = "Sun School"

    def __init__(self, name):
        self.name = name

student = Student("Asha")
print(Student.school)
print(student.name)
