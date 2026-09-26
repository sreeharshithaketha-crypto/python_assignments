# Program 53: Find method

text = "Python Programming"
position = text.find("Programming")

print(f"String: {text}")
print(f"Position of 'Programming': {position}")

# Not found returns -1
position2 = text.find("Java")
print(f"Position of 'Java': {position2}")
