# Base class for all vehicles
class Vehicle:
    def move(self):
        # Abstract method – should be implemented by each subclass
        raise NotImplementedError("Subclasses should implement this method.")

# Subclass representing a car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass representing a plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass representing a boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Demonstrate polymorphism: all vehicle objects in one list
vehicles = [Car(), Plane(), Boat()]

# Each object behaves differently even though we call the same method
for v in vehicles:
    print(v.move())
