# Tuples = a collection which is ordered and unchangeable/used to group together related data

info = ("Fotios", 14, "male")

print(info.count("Fotios"))

print(info.index("male"))

# -------------------------------
print("----------------------------------")
# -------------------------------

for x in info:
    print(x)

if "Fotios" in info:
    print("Hello Fotios!")

# 26/06/23