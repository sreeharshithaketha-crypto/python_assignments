class InsufficientBalanceError(Exception):
    pass

balance = 5000
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise InsufficientBalanceError("Your account does not have sufficient balance.")
    balance -= amount
    print("Withdrawal successful.")
except InsufficientBalanceError as error:
    print("Transaction failed:", error)
