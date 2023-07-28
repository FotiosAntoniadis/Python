# Loop Control Statements = change a loop's execution from its normal sequence.

# break = used to terminate the loop entirely

while True:
    name = input("What is your name? ")
    if name != "":
        break

# continue = skips to the next iteration of the loop

phone_number = "698-308-9310"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# pass = does nothing, acts as a placeholder

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

#25/06/23