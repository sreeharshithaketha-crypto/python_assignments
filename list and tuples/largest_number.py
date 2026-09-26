# 4. Create a list of numbers and find the largest number without using max().
numbers = [10, 45, 20, 5]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)
