# Program 4: Extract first and last names using slicing

full_name = "Ravi Kumar"
parts = full_name.split()
first_name = parts[0]
last_name = parts[1]

print(f"Full Name: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

# Alternative using slicing
text = "RaviKumar"
first = text[:4]
last = text[4:]
print(f"\nUsing slicing:")
print(f"First: {first}")
print(f"Last: {last}")
