# Walrus Operator -> :=

# New to python 3.8
# Assignment expression aka walrus operator
# Assigns values to variables as part of a larger expression

# Previously, using basics of variables
happy = True
print(happy)

# Now, with walrus operator
print(happy := True)

print("--------------------------------------------")

# Previously, with the basics
foods = list()

while True:
    food = input("What food do you like? ")
    if food == "quit":
        break
    foods.append(food)

print("--------------------------------------------")

# Now, with walrus operator

foods2 = list()

while food2 := input('What food do you like? ') != "quit":
    foods.append(food2)

# 09/07/23