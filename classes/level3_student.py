# Q1: Use a class variable college_name with three students.
class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

for student in [Student("Asha"), Student("Ravi"), Student("Mina")]:
    print(student.name, student.college_name)
