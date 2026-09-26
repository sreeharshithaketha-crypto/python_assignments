# Level 3: Constructors & Variables - Question 6 (Employee Subclasses)
# Create an abstract class Employee with name and salary variables. Create subclasses Manager, Developer, and Tester.
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    pass

class Developer(Employee):
    pass

class Tester(Employee):
    pass
