# Program 27: String immutability explanation

name = "Ravi"
print(f"Original: {name}")

# Correct approach to modify
name = "K" + name[1:]
print(f"Modified: {name}")
