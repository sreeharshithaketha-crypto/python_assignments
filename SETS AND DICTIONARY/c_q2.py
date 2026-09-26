# 2. Create a list of student names with duplicates and create a dictionary containing each student's name and number of occurrences.
names = ["Asha", "Ravi", "Asha", "Neha", "Ravi"]
counts = {}
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
