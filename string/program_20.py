# Program 20: Create a URL slug from a course title

title = "Python Full Stack Development Course"
slug = title.lower().replace(" ", "-")

print("Original Title:", title)
print("URL Slug:", slug)
