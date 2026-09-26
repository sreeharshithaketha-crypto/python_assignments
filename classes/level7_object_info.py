# Q3: Create a method that returns another object's information.
class Student:
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name

class School:
    def get_student_info(self, student):
        return student.info()

print(School().get_student_info(Student("Ravi")))
