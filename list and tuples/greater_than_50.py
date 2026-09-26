# 7. Create a list of numbers and count how many numbers are greater than 50.
numbers = [25, 60, 75, 40, 90]
count = 0
for number in numbers:
    if number > 50:
        count = count + 1
print(count)
