# Q1: Create a Student class with a display method.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

Student("Asha", 18).display()
