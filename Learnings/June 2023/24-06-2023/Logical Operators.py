# Logical Operators (and, or, 'not') = used to check if two or more conditional statements are true

kcal = int(input("How many calories did you consume today? "))

if kcal >= 1500 and kcal <= 2500:
    print("That's the normal consumption for maintenance and overall health for teens")

elif kcal < 1500 or kcal > 2500:
    print("The type of your consumption is characterized as unhealthy. You need to find balance.")

#24/06/23