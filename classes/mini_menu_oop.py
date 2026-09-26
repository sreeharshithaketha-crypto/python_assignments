# Mini Project 10: Menu-style OOP application using classes and methods.
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def display(self):
        print(self.name)

students = []
while False:
    print("1. Add  2. Display  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        students.append(Student(input("Name: ")))
    elif choice == "2":
        for student in students:
            student.display()
    else:
        break

student = Student("Example")
student.display()
print("Students:", Student.count)
