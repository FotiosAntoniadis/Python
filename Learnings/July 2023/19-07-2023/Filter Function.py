# filter() = creates a collection of elements from an iterable for which a function returns True
#
# filter(function, iterable)

students = [("Maria", 18),
            ("Giorgos", 19),
            ("Eleni", 20),
            ("Erdogan", 13),
            ("Jimys", 14)]

grades = lambda grades: grades[1] >= 17

Aristouxoi = list(filter(grades, students))

for i in Aristouxoi:
    print(i)

# 19/07/23