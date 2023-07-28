try:
    with open("Read_A_File_Test.txt") as file:
      print(file.read())
except FileNotFoundError:
    print("That file was not found")

# Close or see if closed a file
# print(file.closed)

# Can prevent errors in file location with exception handling

#02/07/23