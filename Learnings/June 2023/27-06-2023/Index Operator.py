# Index Operator [] = Gives access to a sequence's element (str, list, tuples)

name = "deeznuts"

if(name[0].islower()):
    name = name.capitalize()
print(name)


first_name = name[0:4].upper()
print(first_name)

last_name = name[4:9].lower()
print(last_name)

last_character = name[-1]
print(last_character)

# Continue-ing of Str Slicing. 27/06/23