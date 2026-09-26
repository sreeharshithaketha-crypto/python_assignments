# Level 5: Abstract + Concrete Methods - Question 4 (BankAccount)
# Create an abstract BankAccount class with an abstract method calculate_interest() and a normal method display_balance().
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def display_balance(self):
        return "balance"

    @abstractmethod
    def calculate_interest(self):
        pass

class Savings(BankAccount):
    def calculate_interest(self):
        return 0.03
