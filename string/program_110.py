# Program 110: Invoice message

customer = "Ravi Kumar"
amount = 12500.50
invoice_number = 125

message = (
    f"Invoice #{invoice_number:04d}\n"
    f"Customer: {customer}\n"
    f"Amount: ₹{amount:.2f}"
)

print(message)
