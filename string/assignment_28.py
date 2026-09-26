# Assignment Question 28: Write a vowel-counting program

text = input("Enter text: ").lower()
vowels = "aeiou"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Vowel Count:", count)
