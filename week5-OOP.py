class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.battery_level = 100

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def charge(self, minutes):
        self.battery_level += minutes // 10

    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")


phone1 = Smartphone("Apple", "iPhone 14", 128, "Black")
phone2 = Smartphone("Samsung", "Galaxy S23", 256, "White")



class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Dog is running 🐶")

class Cat(Animal):
    def move(self):
        print("Cat is walking 🐱")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")


animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.move()
