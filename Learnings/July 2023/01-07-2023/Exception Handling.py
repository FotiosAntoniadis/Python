# Exception = events detected during execution that interrupt the flow of a program

# numerator = int(input("Enter a number to divide: "))
# denominator = int(input("Enter a number to divide by: "))
# result = numerator/denominator
# print(result)

# If we place n=5, d=0 we get an error/exception

print("------------------------------------------------------")

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError: # as e:
#    print(e) optional, tells the user for the error
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")

# Now the system doesn't pop up an error

# 01/07/23