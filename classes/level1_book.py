# Q5: Create two Book objects and display their details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Basics", "Raj", 300)
book2 = Book("Learn Coding", "Maya", 400)
print(book1.title, book1.author, book1.price)
print(book2.title, book2.author, book2.price)
