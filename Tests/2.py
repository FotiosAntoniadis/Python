action = print

from abc import ABC, abstractmethod

import shutil

import os

import math


class User():

    def Use_app(self):
        action("This user is using the app/game.")
        return self

    def Quit(self):
        action("This user left the game")
        return self


class Human(User):

    def Spawn(self):
        print("This user spawned")
        return self

    def Suicide(self):
        action("This user commited suicide succesfully")
        return self

    def Respawn(self):
        action("This user respawned.")
        return self

    @abstractmethod
    def Die(self):
        action("This user died.")
        return self


# human, we mean player/character


class Villain(Human):

    def Bad(self):
        action("This user is destroying the city!")
        return self


class Hero(Human):

    def Good(self):
        action("This user is saving the city!")
        return self


class BlackAdam(Hero, Villain):
    pass



class TobeyMaguire():
    def Web(self):
        action("This user is shooting webs.")

    def Climb(self):
        action("This user is climbing.")


class MilesMorales():
    def Web(self):
        action("This user is shooting webs.")

    def Climb(self):
        action("This user is climbing.")



class MathGames():
    def Number1(self, x):
        return x+2

try:
    x = int(input("Type a number and we'll get it up by 2: "))

    print(MathGames.Number1(1, x))

except ValueError:
    print('You did not type a number (without decimals).')

print("------------------------------------------------")

# Now, let's test:

a_user = Villain()

a_user.Use_app().Spawn().Bad().Die().Quit()


class Fly():

    def Fly(self):
        action("This user is flying")

class Superman(Fly):

    def Fly(self):
        action("Superman is flying")


print("------------------------------------------------")

print("You throw 3 hit, that equals 20*3=60 damage!")
total_damage = lambda hits, damage: hits*20*damage

print(total_damage(3, 1))

print("------------------------------------------------")

#shutil.copyfile("Project2Modules.txt", "Project2Modules2.txt")

print("------------------------------------------------")

print("Your {0} is so {1}".format("mom", "fat"))

print("------------------------------------------------")

#path = "Project2Modules.txt"
#path2 = "Project2Modules2.txt"

#os.remove(path)
#os.remove(path2)

print("------------------------------------------------")
haha1 = list()

while haha2 := input("haha?: ") != "quit":
    haha1.append(haha2)

print("------------------------------------------------")

number = 3

print(float(int(abs(number))))

print("------------------------------------------------")

website = "www.google.com"

webname = website[4:10]
print(webname)

print("------------------------------------------------")


def Name(**name):
    print("Hello " + name["First"] + " " + name["Middle"] + " " + name["Last"] + ".")


Name(Middle="Big", Last="Nuts", First="Deez")


print("------------------------------------------------")


def haha(*test):
    test = list(test)
    haha = ""
    test.append(haha)
    print(test)


haha(haha(2, "yes", "skibidi", "haha"))

print("------------------------------------------------")

test_subjects = [("Giorgos"),
                 ("Alexandra"),
                 ("Billy"),
                 ("Dimitri")]

test_subjects.sort()

for i in test_subjects:
    print(i)

print("------------------------------------------------")


class SpidermanWebs():
    def __init__(self, durability, lenght):
        self.durability = durability
        self.lenght = lenght


class TMoguire(SpidermanWebs):
    def __init__(self, durability, lenght):
        super().__init__(durability, lenght)

    def Nice(self):
        return self.durability*self.lenght
# the original web, the one from the hand, not the machine


class AGarfield(SpidermanWebs):
    def __init__(self, durability, lenght, cost):
        super().__init__(durability, lenght)
        self.cost = cost

    def Nice2(self):
        return self.durability*self.lenght*self.cost
# The machine, not the organic shooter


print("------------------------------------------------")

Alcohol_In_West = [("Drink_1", 5.00),
                   ("Drink_2", 7.50),
                   ("Drink_3", 10.00),
                   ("Drink_4", 15.00)]

Alcohol_For_DegenWomen = lambda prices: (prices[0], prices[1]-15.00)

DegenWomen = map(Alcohol_For_DegenWomen, Alcohol_In_West)

for i in DegenWomen:
    print(i)

print("------------------------------------------------")


class Toy():
    color = None


def change_color(toy, color):
    toy.color = color


horse = Toy()
change_color(horse, "brown")
print(horse.color)

print("------------------------------------------------")


def write(function):
    text = function("aHhHhHhHhH!")
    print(text)


def pain(text):
    return text.lower()


def PAIN(text):
    return text.upper()


write(pain)
write(PAIN)

# 11/07/23 - 13/07/23 and 18/07/23 - 19/07/23