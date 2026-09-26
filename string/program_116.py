# Program 116: Difference between find and index

text = "Python Programming"

# Find method
print(f"find('Python'): {text.find('Python')}")
print(f"find('Java'): {text.find('Java')}")

# Index method
print(f"index('Python'): {text.index('Python')}")

try:
    print(f"index('Java'): {text.index('Java')}")
except ValueError as e:
    print(f"Error: {e}")
