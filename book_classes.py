# Base class representing a generic book
class Book:
    def __init__(self, title, author, pages):
        # Initialize title, author, and pages (pages is protected with a single underscore)
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulation: protected attribute

    # Method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    # Method to simulate reading the book
    def read(self):
        return f"You start reading '{self.title}'."

# Subclass representing an electronic book (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        # Call the parent constructor using super()
        super().__init__(title, author, pages)
        # Add an additional attribute specific to eBooks
        self.file_size = file_size  # in MB

    # Override the describe() method to include file size
    def describe(self):
        return f"'{self.title}' (eBook) by {self.author}, {self._pages} pages, {self.file_size}MB."

    # Additional method for downloading an eBook
    def download(self):
        return f"Downloading '{self.title}'..."

# Example objects of each class
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Sapiens", "Yuval Noah Harari", 443, 5)

# Output to test functionality
print(book1.describe())
print(book1.read())
print(ebook1.describe())
print(ebook1.download())
