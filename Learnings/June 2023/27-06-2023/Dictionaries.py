# Dictionary = A changeable, unordered collection of key:value pairs.
# Fast, because they use hashing, allow us to access a value quickly.

capitals = {"Greece": "Athens",
            "Turkey": "Ankara",
            "Cyprus": "Nicosia"}

# Print "Athens" using the dictionary
print(capitals["Greece"])

# Check if a keyword is in the dictionary
print(capitals.get("Italy"))

# Print only the keywords
print(capitals.keys())

# Print only the values
print(capitals.values())

# Print Everything
print(capitals.items())

# OR

for key, value in capitals.items():
    print(key, value)

# Update a dictionary with a new keyword and value
capitals.update({"Italy": "Rome"})

print(capitals["Italy"])

# Update a keyword's value
capitals.update({"Greece": "Nauplio"})

print(capitals["Greece"])

# Remove a keyword and value
capitals.pop("Italy")

# Remove everything
capitals.clear()

# 27/06/23