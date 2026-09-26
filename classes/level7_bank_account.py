# Q6: Prevent withdrawal when the balance is insufficient.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal complete")
        else:
            print("Insufficient balance")

account = BankAccount(1000)
account.withdraw(1500)
