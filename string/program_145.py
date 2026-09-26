# Program 145: Advanced string analysis

text = "Python is great and Python is powerful"

analysis = {
    "Total characters": len(text),
    "Total words": len(text.split()),
    "Uppercase letters": sum(1 for c in text if c.isupper()),
    "Lowercase letters": sum(1 for c in text if c.islower()),
    "Digits": sum(1 for c in text if c.isdigit()),
    "Spaces": text.count(" "),
    "Python count": text.count("Python"),
}

print(f"Text: {text}")
print("\nAnalysis:")
for key, value in analysis.items():
    print(f"  {key}: {value}")
