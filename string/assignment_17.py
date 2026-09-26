# Assignment 17: Explain join()

# join() method combines multiple strings into one string
# Syntax: separator.join(list_of_strings)

courses = ["Python", "Java", "Data Science"]
result = ", ".join(courses)

print(f"List: {courses}")
print(f"After join: {result}")

words = ["Python", "Full", "Stack"]
result2 = "-".join(words)
print(f"\nList: {words}")
print(f"After join with hyphen: {result2}")
