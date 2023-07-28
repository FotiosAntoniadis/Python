import os
import shutil

# Delete File:
path = "Delete_a_File_Test.txt"

try:
   os.remove(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that file")
    
# Delete Empty Folder/Directory:
path2 = "Delete File Test"
try:
    os.rmdir(path2)
#       ^
# short for: remove directory
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that file")
except OSError:
    "That file can't be deleted (It has files)"
else:
    print(path2 + " was deleted")

# Delete Folder/Directory with files
path3 = "Delete a File Test Tree"

try:
    shutil.rmtree(path3)
#            ^
# Short for: remove tree
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that file")
else:
    print(path2 + " was deleted")


#02/07/23 - 03/07/23