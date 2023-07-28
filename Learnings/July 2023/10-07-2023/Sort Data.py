# sort() method = used with lists
# sorted() function = used with iterables

students = ["Giannis", "Giorgos", "Maria", "Eleni"]

# Sort by alphabetical character:
students.sort()

for i in students:
    print(i)

print("--------------------------------------------------------")

# Sort by alphabetical character (reversed):
students.sort(reverse=True)

for x in students:
    print(x)

print("--------------------------------------------------------")

# sorted() function
sorted_students = sorted(students)

for z in sorted_students:
    print(z)

print("--------------------------------------------------------")

users = [("Giorgos", "B", 15),
         ("Giannis", "C", 14),
         ("Maria", "D", 13),
         ("Eleni", "A", 16)]

# sort by first column:
users.sort()

for g in users:
    print(g)

print("--------------------------------------------------------")

# sort by second column
grade = lambda grades:grades[1]
users.sort(key=grade)

for o in users:
    print(o)

print("--------------------------------------------------------")

# sort by third column
ages = lambda ages:ages[2]
users.sort(key=ages)

for t in users:
    print(t)

print("--------------------------------------------------------")

# if data is in a tuple, use sorted() function.

# 10/07/23