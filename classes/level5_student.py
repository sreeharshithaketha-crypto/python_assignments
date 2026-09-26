# Q1: Use __init__ to initialize student details and marks.
class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

student = Student("Asha", 18, "BCA", 85)
print(student.name, student.age, student.course, student.marks)
