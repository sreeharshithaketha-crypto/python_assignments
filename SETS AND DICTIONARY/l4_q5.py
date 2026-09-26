# 5. Create a dictionary and calculate the total of all numeric values without using sum().
numbers = {"a": 10, "b": 20, "c": 30}
total = 0
for number in numbers.values():
    total += number
print(total)
