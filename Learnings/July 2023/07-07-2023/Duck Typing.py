# Duck typing = concept where the class of an object is less important than the methods/atributes
# class type is not checked if minimum methods/atributes are present
# If it walks like a duck, and it quacks like a duck, then it must be a duck

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the animal")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

print("--------------------------------------")

person.catch(chicken)

# It prints, even when we requested a "duck" object, due to the 2 classes having same functions.
# If the 2 classes don't have all same functions, an error pops up

# 07/07/23