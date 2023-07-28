# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
#    print("Hello, mr. " + kwargs["first"] + " " + kwargs["last"] + ".")
# First way ^^^, Second way with for loops
    print("Hello ", end="")
    for key, value in kwargs.items():
        print(value, end="")


hello(title="Mr. ", first="Deez ",middle="Big ", last="Nuts")

#29/06/23