# Mini Project 7: Simple school management system.
class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name

student = Student("Asha")
teacher = Teacher("Mr. Kumar")
course = Course("Python")
print(student.name, teacher.name, course.name)
