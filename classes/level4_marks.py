# Q8: Calculate total marks and average marks.
class Student:
    def total_marks(self, marks):
        return sum(marks)

    def average_marks(self, marks):
        return sum(marks) / len(marks)

student = Student()
marks = [80, 70, 90]
print(student.total_marks(marks))
print(student.average_marks(marks))
