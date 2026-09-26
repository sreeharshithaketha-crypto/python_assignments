# Assignment 18: Differentiate between find() and index()

# find() returns -1 when substring is not found
# index() raises ValueError when substring is not found

text = "Python Programming"

# find()
print(f"find('Programming'): {text.find('Programming')}")
print(f"find('Java'): {text.find('Java')}")

# index()
print(f"index('Python'): {text.index('Python')}")

try:
    print(f"index('Java'): {text.index('Java')}")
except ValueError as e:
    print(f"index('Java') raised error: {e}")
