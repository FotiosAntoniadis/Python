class Animal:

    alive = True

    def eat(self):
        print("The is eating")

    def sleep(self):
        print("This Animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

print("------------------------------------------")

rabbit.run()
fish.swim()
hawk.fly()

# 05/07/23