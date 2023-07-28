# reduce() = apply a function to an iterable and reduce it to a single cumulative value
# performs function on firsttwo elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x, y: x+y, letters)
print(word)

print("---------------------------------------------")
# factorial = 5!

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x*y, factorial)
print(result)

#20/07/23