# 15. Create a dictionary containing numbers from 1 to 10 as keys and their cubes as values.
cubes = {}
for number in range(1, 11):
    cubes[number] = number * number * number
print(cubes)
