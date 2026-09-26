# Program 106: Search system

courses = """
Python Programming
Java Full Stack
Data Science
Data Analysis
Digital Marketing
"""

search = input("Search Course: ").strip().lower()

if search in courses.lower():
    print("Course Available")
else:
    print("Course Not Available")
