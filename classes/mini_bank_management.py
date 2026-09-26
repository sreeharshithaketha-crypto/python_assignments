# Mini Project 3: Simple bank management system.
class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

account = Account("101", "Asha", 1000)
account.deposit(500)
account.withdraw(200)
print(account.holder, account.balance)
