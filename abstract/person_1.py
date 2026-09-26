# Level 1: Basic Abstract Classes - Question 7 (Person)
# Create an abstract class Person with an abstract method role(). Implement it using Student and Teacher.
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        return "student"

class Teacher(Person):
    def role(self):
        return "teacher"

if __name__ == "__main__":
    print(Student().role())
    print(Teacher().role())
