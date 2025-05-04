# book_classes.py
# Contains the Book and EBook class definitions

class Book:
    def __init__(self, title, author, pages):
        # Initialize book attributes
        self.title = title
        self.author = author
        self._pages = pages  # Protected attribute (encapsulation)

    def describe(self):
        # Return a description of the book
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    def read(self):
        # Simulate reading the book
        return f"You start reading '{self.title}'."

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        # Initialize EBook using the parent constructor and add file_size
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def describe(self):
        # Override the describe method to include file size
        return f"'{self.title}' (eBook) by {self.author}, {self._pages} pages, {self.file_size}MB."

    def download(self):
        # Simulate downloading the ebook
        return f"Downloading '{self.title}'..."

