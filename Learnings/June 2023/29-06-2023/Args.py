# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*test):
    sum = 0
    test = list(test) # Convert tuple to list
    test[0] = 0 # Change values in the list
    for i in test:
       sum += i
    return sum


print(add(1, 2, 3, 4, 6))

#29/06/23