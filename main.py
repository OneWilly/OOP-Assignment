# main.py
# Runs example code from both assignments(book_classes.py & vehicle_polymorphism.py)


from book_classes import Book, EBook
from vehicle_polymorphism import Car, Plane, Boat

# ----------------------------
# Assignment 1: Book Examples
# ----------------------------
print("📚 Assignment 1: Book & EBook\n")

# Create instances of Book and EBook
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Sapiens", "Yuval Noah Harari", 443, 5)

# Print details and behaviors
print(book1.describe())
print(book1.read())
print(ebook1.describe())
print(ebook1.download())

# ----------------------------
# Activity 2: Vehicle Polymorphism
# ----------------------------
print("\n🎭 Activity 2: Vehicle Polymorphism\n")

# Create a list of different vehicle types
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphic move() behavior
for vehicle in vehicles:
    print(vehicle.move())
