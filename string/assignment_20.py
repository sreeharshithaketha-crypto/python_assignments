# Assignment 20: Explain startswith() and endswith()

# startswith() checks if string begins with specified text
# endswith() checks if string ends with specified text

website = "https://www.example.com"
filename = "report.pdf"

print(f"Website: {website}")
print(f"Starts with 'https': {website.startswith('https')}")
print(f"Starts with 'http': {website.startswith('http')}")

print(f"\nFilename: {filename}")
print(f"Ends with '.pdf': {filename.endswith('.pdf')}")
print(f"Ends with '.txt': {filename.endswith('.txt')}")
