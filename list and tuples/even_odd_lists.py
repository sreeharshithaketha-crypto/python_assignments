# 8. Create a list of numbers and create separate lists for even and odd numbers.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)
