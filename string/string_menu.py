# Make a simple string menu program.
while True:
    print("1 Reverse  2 Palindrome  3 Vowels  4 Words")
    print("5 Frequency  6 Uppercase  7 Lowercase  8 Exit")
    choice = input("Choose: ")
    if choice == "8":
        break
    text = input("Enter string: ")
    if choice == "1":
        print(text[::-1])
    elif choice == "2":
        print(text == text[::-1])
    elif choice == "3":
        print(sum(char.lower() in "aeiou" for char in text))
    elif choice == "4":
        print(len(text.split()))
    elif choice == "5":
        for char in sorted(set(text)):
            print(char, text.count(char))
    elif choice == "6":
        print(text.upper())
    elif choice == "7":
        print(text.lower())