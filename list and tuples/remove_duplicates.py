# 9. Create a list containing duplicate values and create a new list without duplicates. Do not use set().
numbers = [1, 2, 2, 3, 4, 4, 5]
new_numbers = []
for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
print(new_numbers)
