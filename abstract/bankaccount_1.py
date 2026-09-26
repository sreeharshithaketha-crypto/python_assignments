# Level 1: Basic Abstract Classes - Question 8 (BankAccount)
# Create an abstract class BankAccount with an abstract method calculate_interest(). Implement it using SavingsAccount and CurrentAccount.
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0.0

if __name__ == "__main__":
    print(SavingsAccount().calculate_interest())
    print(CurrentAccount().calculate_interest())
