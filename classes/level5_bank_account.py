# Q5: Create a BankAccount with an initial balance.
class BankAccount:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

account = BankAccount("Anu", "1234", 5000)
print(account.holder, account.number, account.balance)
