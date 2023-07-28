# lambda function = function written in 1 line using lambda keyword
# acceptsany number of arguments, but only has one expression
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

# Previously, with the basics
def double(x):
    return x*2

print(double(5))

print("--------------------------------------------------")

# Now, with lambda functions
double2 = lambda x:x*2
print(double2(5))

print("--------------------------------------------------")

# Another example
multiply = lambda x, y: x*y

print(multiply(5, 7))

print("--------------------------------------------------")

# Another Another Example
add = lambda x,y,z: x+y+z

print(add(2, 2, 2))

# 10/07/23