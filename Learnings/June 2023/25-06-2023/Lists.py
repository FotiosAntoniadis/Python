# List = used to store multiple items in a single variable

food = ["dolma", "borek", "gyros", "steak"]

print(food[0])
# print dolma

food.append("pizza")
# add "pizza" in the list

food.remove("pizza")
# remove "pizza" from the list

food.pop()
# remove last value from list

food.insert(0, "Pastitsio")
#add a value in a definitive place

food.sort()
#sort a list alphabetically

food.clear()
#delete values from a list

for x in food:
    print(x)

#25/06/23