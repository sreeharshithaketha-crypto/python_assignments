# Level 6: Real-World Practice - Question 3 (HospitalEmployee)
# Create an abstract HospitalEmployee class and implement Doctor, Nurse, and Pharmacist classes.
from abc import ABC, abstractmethod

class HospitalEmployee(ABC):
    @abstractmethod
    def duty(self):
        pass

class Doctor(HospitalEmployee):
    def duty(self):
        return "treat"

class Nurse(HospitalEmployee):
    def duty(self):
        return "care"

class Pharmacist(HospitalEmployee):
    def duty(self):
        return "dispense"
