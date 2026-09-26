# Program 144: String transformation examples

text = "python programming"

transformations = {
    "Original": text,
    "Uppercase": text.upper(),
    "Capitalized": text.capitalize(),
    "Title": text.title(),
    "Reversed": text[::-1],
    "Sorted": "".join(sorted(text)),
}

for name, result in transformations.items():
    print(f"{name}: {result}")
