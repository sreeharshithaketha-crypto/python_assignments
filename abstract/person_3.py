# Level 3: Constructors & Variables - Question 7 (Person)
# Create an abstract class Person with name and age. Create subclasses Student, Teacher, and Doctor.
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    pass

class Teacher(Person):
    pass

class Doctor(Person):
    pass
