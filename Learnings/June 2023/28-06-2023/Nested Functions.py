# Nested Functions Calls = function calls inside other function calls
# Innermost function calls are resolved first
# Returned value is used as argument for the next outer function

#Previously used (Technique to not let user enter negative number):
number = input("What is your favorite positive number? ")
number = float(number)
number = abs(number)
number = round(number)
print(number)

# Now, with nested function calls
print(round(abs(float(input("What is your favorite positive number (2) ? ")))))

#28/06/23