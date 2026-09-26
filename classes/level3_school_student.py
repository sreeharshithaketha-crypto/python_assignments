# Q7: Use a class variable for school and an instance variable for name.
class Student:
    school_name = "Sun School"

    def __init__(self, name):
        self.name = name

student = Student("Asha")
print(student.name, student.school_name)
