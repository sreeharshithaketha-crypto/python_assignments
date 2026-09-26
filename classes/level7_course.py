# Q9: Store enrolled students and display them.
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def display_students(self):
        print(self.students)

course = Course("Python")
course.enroll("Asha")
course.enroll("Ravi")
course.display_students()
