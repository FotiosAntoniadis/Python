# Set = a collection which is unordered, un-indexed. No duplicate values.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#METHODS:

# Add a value/element
utensils.add("napkin")

# Remove an element/value
utensils.remove("napkin")

# Remove all elements/values
#utensils.clear()

# Update the set
utensils.update(dishes)

# Add both sets into one
dinner_table = utensils.union(dishes)


for x in dinner_table:
    print(x)
# every time it is printed, the order is different

# Difference between two sets
print(utensils.difference(dishes))

# Commons between two sets
print(utensils.intersection(dishes))

# 27/06/23