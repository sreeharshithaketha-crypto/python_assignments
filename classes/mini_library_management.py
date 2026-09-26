# Mini Project 4: Simple library management system.
class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        self.issued = True

    def return_book(self):
        self.issued = False

books = [Book("Python"), Book("Math")]
books[0].issue()
print(books[0].title, books[0].issued)
books[0].return_book()
print(books[0].title, books[0].issued)
