# Program 10: Count digits and spaces

text = input("Enter sentence: ")
digit_count = 0
space_count = 0

for character in text:
    if character.isdigit():
        digit_count += 1
    elif character == " ":
        space_count += 1

print("Digit Count:", digit_count)
print("Space Count:", space_count)
