# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
# creates a zip object with paired elements stored in tuples for each element within our zip object.

usernames = ["DeezNuts", "XxEpicGamer69xX", "-Full name-"]
passwords = ("Ha! Got'em!", "FortniteOnTop", "-Fullname--Birtday-")
login_date = ["11/09/2010", "05/04/2021", "Today"]

users = zip(usernames, passwords, login_date)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# use list() or dict() to turn this zipped tuple into a list or dictionary

print(type(users))

for i in users:
    print(i)

# 22/07/23