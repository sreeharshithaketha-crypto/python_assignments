# Assignment 16: Explain split()

# split() method converts a string into a list
# By default, it splits by spaces

courses = "Python,Java,Data Science"
result = courses.split(",")

print(f"String: {courses}")
print(f"After split: {result}")

sentence = "Python is easy to learn"
words = sentence.split()
print(f"\nSentence: {sentence}")
print(f"Words: {words}")
