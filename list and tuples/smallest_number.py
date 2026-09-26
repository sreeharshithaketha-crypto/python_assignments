# 5. Create a list of numbers and find the smallest number without using min().
numbers = [10, 45, 20, 5]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)
