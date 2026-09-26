# Program 117: Difference between split and join

text = "Python,Java,SQL"

# Split: string to list
courses = text.split(",")
print(f"Original: {text}")
print(f"After split: {courses}")

# Join: list to string
result = " | ".join(courses)
print(f"After join: {result}")
