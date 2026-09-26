# Q7: Calculate a student's grade from marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        if self.marks >= 75:
            return "B"
        if self.marks >= 50:
            return "C"
        return "F"

student = Student("Asha", 82)
print(student.name, student.grade())
