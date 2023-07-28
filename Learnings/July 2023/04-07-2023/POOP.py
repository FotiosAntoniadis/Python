# Python Object Oriented Programming

# An object is an instance of a class. A class ia a "blueprint" of an object.

# Atributes = what an object is or has:
class Car:
    # Init for initialize. The constructor module
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

# Methods = what the object can do:
    def drive(self):
        print("This " + self.model + " is driving.")

    def stop(self):
        print("This " + self.model + " is stopped.")

# Construct an object


car_1 = Car("Ferrari", "Formula1", 2022, "Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print("--------------------------")

car_1.drive()
car_1.stop()

print("--------------------------")

car_2 = Car("Mercedes", "Benz", 2023, "Blue")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

print("--------------------------")

car_2.drive()
car_2.stop()

# 04/07/23