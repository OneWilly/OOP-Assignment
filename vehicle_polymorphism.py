# vehicle_polymorphism.py
# Contains Vehicle class and its polymorphic subclasses

class Vehicle:
    def move(self):
        # Abstract method to be overridden
        raise NotImplementedError("Subclasses should implement this method.")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"
