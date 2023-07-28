# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

#Previously:
# print("The " + animal + " jumped over the " + item + ".")

print("The {} jumped over the {}".format("cow", "moon"))
#                                         ^        ^
#                                        animal   item

#OR

print("The {0} jumped over the {1}".format("cow", "moon"))
# Positional Argument                        ^      ^
#                                            0      1    ...

# OR

print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))
# Keyword Argument

# In all ways mentioned above, we can put 1 value twice, eg. "cow"-"cow", 1-1, animal-animal


# Another Way:

text = "The {} jumped over the {}"
print(text.format(animal, item))

print("---------------------------------------------------------")

name = "Deez"

print("Hello, my name is {}".format(name))

# Extra Room:
print("Hello, my name is {:10}. Nice to meet you".format(name))

# Left Align:
print("Hello, my name is {:<10}. Nice to meet you".format(name))

# Right Align:
print("Hello, my name is {:>10}. Nice to meet you".format(name))

# Center Align:
print("Hello, my name is {:^10}. Nice to meet you".format(name))

print("---------------------------------------------------------")

number = 3.14159

# Show only two first decimals:
print("The number p is {:.2f}".format(number))
#                          ^ f = float

number2 = 6900

# Place commas in the right positions
print("The number is {:,}".format(number2))

# Display number as binary
print("The number is {:b}".format(number2))

# Display number as octal
print("The number is {:o}".format(number2))

# Display number as hexadecimal
print("The number is {:X}".format(number2))
# X or x for uppercase and lowercase

# Display number in scientific notation
print("The number is {:e}".format(number2))
# E or e for uppercase or lowercase

# 30/06/23