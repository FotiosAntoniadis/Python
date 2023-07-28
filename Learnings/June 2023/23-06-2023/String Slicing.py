# Slicing = Create a substring by extracting elements from another string

# 2 ways: "indexing[]" or "slice()"
# 3 arguments: [start:stop:step]

#First, x[]:

Name = "Deez Nuts"
#       ^^^^^^^^^^
#       0123456789

First_name = Name[0:4]
print(First_name)

Last_Name = Name[5:9]
print(Last_Name)

Goofy_Name = Name[0:9:2]
print(Goofy_Name)

Reversed_Name = Name[::-1]
print(Reversed_Name)

#---------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------")
#---------------------------------------------------------------------------------

# Second, slice():

website1 = "https://sites.google.com/view/pontosinfo "
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#          12345678901234567890123456789012345678901

slice = slice(30, -1)

print(website1[slice])

website2 = "https://sites.google.com/view/randomwebsiteIDK "

print(website2[slice])

#23/06/23