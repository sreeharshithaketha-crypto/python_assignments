# Program 140: String method chaining practice

text = "  hello WORLD from PYTHON  "

# Chain multiple methods
result = text.strip().lower().replace("world", "everyone").title()

print(f"Original: '{text}'")
print(f"Result: '{result}'")
