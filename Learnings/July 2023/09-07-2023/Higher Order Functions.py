# Higher Order Function =  A function that either:
#                          1. Accepts a function as an argument
#                                        OR
#                          2. Returns a function
#                   (In python, functions are also treated as objects)


# The Employees:
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()

# The Boss (He takes the text and give it to the wanted employee) :
def hello(function):
    text = function("HeLlO")
    print(text)


hello(loud)
hello(quiet)

print("--------------------------------------------------------------")


def divisor(x):       # nested function
    def dividend(y):
        return (y/x)
    return dividend


divide = divisor(2)
# divide is a variable for the divisor function and the number in the parenthesis is the dividend

print(divide(10))

# 09/07/23