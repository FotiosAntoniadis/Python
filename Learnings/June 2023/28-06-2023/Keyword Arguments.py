# Keyword Arguments = arguments preceded by an identifier when we pass them to functions
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives


# Positional arguments (the ones we used until now):
def hello(first, middle, last):
    print("Hello " + first + middle + last)


hello("Deez", "Big", "Nuts")


# Keyword Arguments:
def hello(first, middle, last):
    print("Hello " + first + middle + last)


hello(last="Nuts", first="Deez", middle="Big")

# 28/26/23