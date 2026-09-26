# Level 3: Constructors & Variables - Question 4 (BankAccount)
# Create an abstract class BankAccount with account holder and account number. Add an abstract method calculate_interest().
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

class SimpleSavings(BankAccount):
    def calculate_interest(self):
        return 0.03
