# Mini Project 3: Hospital Management System
# Build a Hospital Management System using abstract classes for doctors, nurses, and other hospital employees.
from abc import ABC, abstractmethod

class Staff(ABC):
    @abstractmethod
    def duty(self):
        pass

class Doctor(Staff):
    def duty(self):
        return "treat"
