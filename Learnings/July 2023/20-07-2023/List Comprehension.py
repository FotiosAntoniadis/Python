# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [-expression- (if/else) "for" -item- "in" -iterable- *if conditional*]

# Previously:
squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

print("--------------------------------------------")

# Now, with list comprehension:
squares = [i*i for i in range(1, 11)]
print(squares)

print("--------------------------------------------")

# Previously:
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

passed_students = list(filter(lambda x: x >= 50, students))

print(passed_students)

print("--------------------------------------------")

# Now, with list comprehension:
passed_students = [i for i in students if i >= 50]
print(passed_students)

print("--------------------------------------------")

# Another way:
passed_students = [i if i >= 50 else "FAILED" for i in students]
print(passed_students)

# 20/07/23