import os

path = "C:\\Users\\Kosma\\Documents\\Φώτη's stuff\\haha.png"

# See if a location exists:
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file") # See if the location is a file
    elif os.path.isdir(path):
        print("That is a directory") # See if the location is a diectory/folder
else:
    print("That location doesn't exist")

# 01/07/23