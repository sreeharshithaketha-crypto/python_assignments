# Level 4: Polymorphism - Question 4 (Employee)
# Create an abstract Employee class and use polymorphism to calculate salaries of different employees.
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Dev(Employee):
    def calculate_salary(self):
        return 4000

class Manager(Employee):
    def calculate_salary(self):
        return 7000
