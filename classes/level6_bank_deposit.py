# Q4: Accept an amount and deposit it into a bank account.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

print(BankAccount(1000).deposit(500))
