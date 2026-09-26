balance = 5000.0
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)
except ValueError as error:
    print("Transaction failed:", error)
finally:
    print("Thank you for using our banking service.")
