# Mini Project 2: E-Commerce Payment System
# Build an E-Commerce Payment System using abstract classes and methods for multiple payment methods.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        return "upi"
