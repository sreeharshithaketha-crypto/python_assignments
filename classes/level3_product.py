# Q5: Use a class variable category for products.
class Product:
    category = "Stationery"

    def __init__(self, name):
        self.name = name

pen = Product("Pen")
book = Product("Book")
print(pen.name, pen.category)
print(book.name, book.category)
