# 6. Create a set of numbers and find the largest number without using max().
numbers = {8, 3, 12, 5}
largest = None
for number in numbers:
    if largest is None or number > largest:
        largest = number
print(largest)
