# Level 6: Real-World Practice - Question 6 (EmployeePayroll)
# Create an abstract EmployeePayroll class and implement FullTimeEmployee, PartTimeEmployee, and ContractEmployee.
from abc import ABC, abstractmethod

class EmployeePayroll(ABC):
    @abstractmethod
    def compute(self):
        pass

class FullTimeEmployee(EmployeePayroll):
    def compute(self):
        return 5000

class PartTimeEmployee(EmployeePayroll):
    def compute(self):
        return 2000

class ContractEmployee(EmployeePayroll):
    def compute(self):
        return 3000
