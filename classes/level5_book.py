# Q3: Use __init__ and a method to display book information.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.title, self.author, self.price)

Book("Python", "Raj", 300).display()
