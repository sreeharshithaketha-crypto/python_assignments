# Mini Project 7: Employee Payroll System
# Build an Employee Payroll System using abstract classes for different employee categories.
from abc import ABC, abstractmethod

class Payroll(ABC):
    @abstractmethod
    def compute(self):
        pass

class FullTime(Payroll):
    def compute(self):
        return 5000
