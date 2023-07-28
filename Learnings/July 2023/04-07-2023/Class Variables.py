# A class variable is declaired inside the class but outside the constructor. A default value that all object of
# our objects type have

class Car:

    wheels = 4 #class variable

    def __init__(self, make, model, year, color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable


car_1 = Car("Kawasaki", "Ninja H2R", 2022, "Black-Green")
car_2 = Car("Mercedes", "Benz", 2023, "Blue")

# Change an object's class variable
car_1.wheels = 2
# Bro, I searched motorbikes for this

print(car_1.wheels)
print(car_2.wheels)

print("------------------------------------")

print(Car.wheels)

# Change class-variable's default value
# Car.wheels = 2

# 04/07/23