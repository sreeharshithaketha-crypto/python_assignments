# Level 2: Multiple Methods - Question 3 (Employee)
# Create an abstract class Employee with abstract methods calculate_salary() and display_details(). Implement them in Manager and Developer.
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 8000
    def display_details(self):
        return "manager details"

class Developer(Employee):
    def calculate_salary(self):
        return 5000
    def display_details(self):
        return "developer details"
