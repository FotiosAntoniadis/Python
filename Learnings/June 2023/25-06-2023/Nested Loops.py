# Nested Loops = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop".

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter the symbol ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

#25/06/23