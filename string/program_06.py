# Program 6: Check whether a string is a palindrome

text = input("Enter a word: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
