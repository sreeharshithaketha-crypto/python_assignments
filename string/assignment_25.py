# Assignment 25: String comparison and conversion

print("=" * 50)
print("ASSIGNMENT 25: String comparison and conversion")
print("=" * 50)

# String comparison
a = "Python"
b = "python"
print(f"'{a}' == '{b}': {a == b}")
print(f"'{a}' < '{b}': {a < b}")

# Case-insensitive comparison
print(f"Case-insensitive: {a.lower() == b.lower()}")

# Type conversion
age_str = "25"
age_int = int(age_str)
price_str = "99.99"
price_float = float(price_str)

print(f"\nString to int: {age_str} -> {age_int}")
print(f"String to float: {price_str} -> {price_float}")

# Int to string
num = 42
text = str(num)
print(f"Int to string: {num} -> {text}")
