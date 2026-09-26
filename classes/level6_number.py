# Q7: Check whether a number is even, odd, prime, or palindrome.
class Number:
    def __init__(self, number):
        self.number = number

    def even(self):
        return self.number % 2 == 0

    def odd(self):
        return self.number % 2 != 0

    def prime(self):
        return self.number > 1 and all(self.number % i != 0 for i in range(2, self.number))

    def palindrome(self):
        return str(self.number) == str(self.number)[::-1]

number = Number(11)
print(number.even(), number.odd(), number.prime(), number.palindrome())
