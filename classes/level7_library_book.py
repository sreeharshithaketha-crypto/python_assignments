# Q7: Create methods to issue and return a library book.
class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        self.issued = True
        print("Book issued")

    def return_book(self):
        self.issued = False
        print("Book returned")

book = LibraryBook("Python")
book.issue()
book.return_book()
