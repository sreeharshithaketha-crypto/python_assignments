# 6. Create a list of numbers and calculate the average.
numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
    total = total + number
average = total / len(numbers)
print(average)
