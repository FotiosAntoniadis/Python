# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract methods = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod
# abc = abstract base class


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")


    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcyrcle")

    def stop(self):
        print("You stop the motorcycle")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

print("------------------------")

car.stop()
motorcycle.stop()

# Commenting those 2 vehicle variables and functions actions, because of error

# 06/07/23