# Program 122: Best practices - strip user input

name1 = input("Enter name without strip: ")
name2 = input("Enter name with strip: ").strip()

print(f"Without strip: '{name1}'")
print(f"With strip: '{name2}'")
