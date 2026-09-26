# 7. Create a set of numbers and find the smallest number without using min().
numbers = {8, 3, 12, 5}
smallest = None
for number in numbers:
    if smallest is None or number < smallest:
        smallest = number
print(smallest)
