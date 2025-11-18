# Base class (Parent)
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def describe(self):
        return f"{self.name} protects {self.city} using {self.power}."

    def attack(self):
        return f"{self.name} attacks with {self.power}!"


# Derived class (Child)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Polymorphism
    def attack(self):
        return f"{self.name} swoops from the sky at {self.flight_speed} km/h using {self.power}!"


# Create objects
hero1 = Superhero("Shadow Knight", "stealth", "Gotham")
hero2 = FlyingHero("Sky Falcon", "wind blasts", "Metropolis", 300)

# Use the objects
print(hero1.describe())
print(hero1.attack())

print(hero2.describe())
print(hero2.attack())  # Uses overridden method!