# Q9: Create a BankAccount object and display its details.
class BankAccount:
    def __init__(self, holder, number):
        self.holder = holder
        self.number = number

account = BankAccount("Ravi", "12345")
print(account.holder, account.number)
