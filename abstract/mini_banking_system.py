# Mini Project 1: Banking Management System
# Build a Banking Management System using abstract classes for different account types.
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def info(self):
        pass

class Savings(Account):
    def info(self):
        return "savings"

class Current(Account):
    def info(self):
        return "current"
