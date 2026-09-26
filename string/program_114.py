# Program 114: Masking email address

email = "ravi@example.com"
username, domain = email.split("@")
masked = username[0] + "***@" + domain

print(f"Original: {email}")
print(f"Masked: {masked}")
