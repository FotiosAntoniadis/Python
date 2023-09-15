import time

from Project1Modules import *

name, number, fday, age = "", "", "", ""

print("-------------------------------------------")

name = ""

while len(name) == 0:
    name = input("What is your (user)name? ")
    if len(name) > 0:
        print("Hello " + name)
        break
#time.sleep(1)

print("-------------------------------------------")

number = ""



while number == "":
    number = input("What is your favorite number? ")

    if len(number) > 0:
        print(int(number))
        print("Nice Number, " + str(number))



#time.sleep(2)

print("-------------------------------------------")

fday = ""

while fday == "":
    fday = input("What is your favorite day? ")
    if len(fday) > 0:
        print("I wonder why...")
        print(float(fday))
        print("... is your favorite day.")
        break
#time.sleep(3)

print("-------------------------------------------")

age = ""

age = int(input("What is your age? "))
if age > 0 and age < 12:
    print("You are too young to use this program")
    print("If you want to use this program, get back in " + str(13 - age) + " years.")
#    time.sleep(5)
elif age > 12 and age < 65:
    print("So you are " + str(age) + ", huh?")
#    time.sleep(2)
elif age < 0:
    print("Go to your mama's belly. When you learn to talk, get back here in " + str(13 - age) + " years.")
#    time.sleep(5)
else:
    print("A veteran, huh?")
#    time.sleep(2)

#--------------------------------------------------------------------
userinfo = {"Name": name,
            "Favorite Number": number,
            "Favorite Day": fday,
            "Age": age}
#--------------------------------------------------------------------

print("-------------------------------------------")

permission = ""

while permission == "yes" or "no":
    permission = input("Do you give us permission to store your data? Type 'Yes' or 'No': ").lower()
    if permission == "yes":
        print("Thank you.")
        print("-------------------------------------------")
        print("Your name is: " + userinfo["Name"])
        print("Your favorite number is: " + userinfo["Favorite Number"])
        print("Your favorite day is: " + userinfo["Favorite Day"])
        print("Your age is: " + str(userinfo["Age"]))
        break
    elif permission == "no":
        print("Ok. Understandable")
        print("Bye")
        break

print("-------------------------------------------")

# != = not equal

userinfo2 = (name, number, fday, age)
#unchangeable
userinfo3 = [name, number, fday, age]
#changeable

#26/06/23 -

# if name in userinfo:
#    print("Hello " + name)
#(easter egg)

# -------------------------------------------------------------------------------------------------------------

# variables, while loop, str commands, user input, if statement, print, loop control statements, type casting
# , Logical operators,  multiple assignments, math functions, tuples, lists
#--------
# 2D lists, For loops, nested loops, string slicing,

# -------------------------------------------------------------------------------------------------------------

# modules, dictionary, function to variable, POOP, inheritance, multi-level inheritance, multiple inheritance
# duck typing, abstract class, return statement, exception handling,  method chaining, method overiding, class variables
# ,lambda, copy files, format, random module(game), delete file, walrus operator, nested function calls,
# index operator, keyword arguments, functions, args, kwargs, sort data, super() function,  map function,
# objects as arguments, higher order functions

# Theory: variable scope, sets, move files, file detenction, read a file, write files,

# -------------------------------------------------------------------------------------------------------------

# filter(), reduce(), list comprehension, dectionary comprehension, zip function, name='__main__', time module,
# multithreading, daemon threads, multiprocessing, GUI windows, labels , buttons, entrybox, checkbox, radiobutton,
# sliding scale, listbox, messagebox, colorchooser