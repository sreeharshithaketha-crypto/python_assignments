# Level 6: Real-World Practice - Question 1 (ATM)
# Create an abstract ATM class with methods for withdrawal, deposit, and balance checking. Implement it using a concrete bank class.
from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def balance(self):
        pass

class BankATM(ATM):
    def __init__(self):
        self.b=100
    def withdraw(self):
        self.b-=10
        return self.b
    def deposit(self):
        self.b+=10
        return self.b
    def balance(self):
        return self.b
