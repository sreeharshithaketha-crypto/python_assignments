# Q2: Accept marks and return the student's grade.
class Student:
    def grade(self, marks):
        if marks >= 90:
            return "A"
        if marks >= 75:
            return "B"
        if marks >= 50:
            return "C"
        return "F"

print(Student().grade(80))
