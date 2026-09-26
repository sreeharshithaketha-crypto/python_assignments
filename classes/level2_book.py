# Q6: Create multiple Book objects.
class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

books = [Book("Python", "Raj", 300, 200), Book("Math", "Maya", 250, 150)]
for book in books:
    print(book.title, book.author, book.price, book.pages)
