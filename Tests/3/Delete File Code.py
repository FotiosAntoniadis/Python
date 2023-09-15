path = "log.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that file")