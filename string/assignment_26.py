# Assignment Question 26: Write a palindrome program

text = input("Enter text: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
