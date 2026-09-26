# Count uppercase and lowercase characters.
text = "Hello PYthon"
upper = 0
lower = 0
for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)