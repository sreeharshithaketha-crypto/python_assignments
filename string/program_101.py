# Program 101: String identity vs equality

a = "Python"
b = "Python"

print(f"a == b (equality): {a == b}")
print(f"a is b (identity): {a is b}")

# Force different objects
c = "".join(["P", "y", "t", "h", "o", "n"])
print(f"a == c: {a == c}")
print(f"a is c: {a is c}")
