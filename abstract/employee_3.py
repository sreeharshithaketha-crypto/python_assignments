# Level 3: Constructors & Variables - Question 1 (Employee)
# Create an abstract class Employee with a constructor that accepts name and employee ID. Add an abstract method calculate_salary().
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

class SimpleEmployee(Employee):
    def calculate_salary(self):
        return 3000

if __name__ == "__main__":
    e = SimpleEmployee('A', 1)
    print(e.name, e.emp_id, e.calculate_salary())
