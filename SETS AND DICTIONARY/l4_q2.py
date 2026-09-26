# 2. Create a dictionary of numbers and count how many values are even and odd.
numbers = {"a": 2, "b": 5, "c": 8, "d": 9}
even = 0
odd = 0
for number in numbers.values():
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)
