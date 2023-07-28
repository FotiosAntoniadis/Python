import os

# Move a file
source = "Move_Files_Test.txt"
destination = "C:\\Users\\Kosma\\Documents\\Python Test\\Move_a_File_Test.txt"
#                                              Be sure to text the file at the end

try:
    if os.path.exists(destination):
        print("There is alredy a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")


# Move a Folder

source = "Move Files Test Fold"
destination = "C:\\Users\\Kosma\\Documents\\Python Test\\Move a File Test Fold"
#                                              Be sure to text the file at the end

try:
    if os.path.exists(destination):
        print("There is alredy a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

# 02/07/23