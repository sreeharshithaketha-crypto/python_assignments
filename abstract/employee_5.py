# Level 5: Abstract + Concrete Methods - Question 1 (Employee)
# Create an abstract Employee class with one abstract method calculate_salary() and one normal method display_company().
from abc import ABC, abstractmethod

class Employee(ABC):
    def display_company(self):
        return "SimpleCorp"

    @abstractmethod
    def calculate_salary(self):
        pass

class SimpleDev(Employee):
    def calculate_salary(self):
        return 3000
