# Program 125: Reverse string alternative methods

text = "Python"

# Method 1: Slicing
reversed1 = text[::-1]
print(f"Slicing: {reversed1}")

# Method 2: Loop
reversed2 = ""
for char in text:
    reversed2 = char + reversed2
print(f"Loop: {reversed2}")

# Method 3: Reversed function
reversed3 = "".join(reversed(text))
print(f"Reversed function: {reversed3}")
