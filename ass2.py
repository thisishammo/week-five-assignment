class Vehicle:
    def move(self):
        # Base method (can be overridden)
        print("This vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bike(Vehicle):
    def move(self):
        print("Cycling 🚴")
        

# Create objects
car = Car()
plane = Plane()
boat = Boat()
bike = Bike()

# Demonstrate polymorphism
vehicles = [car, plane, boat, bike]

for v in vehicles:
    v.move()   # Same method name, different behavior
