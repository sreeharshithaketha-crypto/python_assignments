# Q4: Use a class variable bank_name for multiple accounts.
class BankAccount:
    bank_name = "Simple Bank"

    def __init__(self, holder):
        self.holder = holder

account1 = BankAccount("Ravi")
account2 = BankAccount("Anu")
print(account1.holder, account1.bank_name)
print(account2.holder, account2.bank_name)
