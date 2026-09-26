# Q8: Reverse a string, count vowels, and check palindrome.
class StringOperations:
    def reverse(self, text):
        return text[::-1]

    def count_vowels(self, text):
        return sum(letter in "aeiouAEIOU" for letter in text)

    def palindrome(self, text):
        return text == text[::-1]

operations = StringOperations()
print(operations.reverse("hello"))
print(operations.count_vowels("hello"))
print(operations.palindrome("level"))
