# Level 3: Constructors & Variables - Question 8 (Account)
# Create an abstract class Account with account number and balance. Implement SavingsAccount and CurrentAccount.
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.03

class CurrentAccount(Account):
    def calculate_interest(self):
        return 0
