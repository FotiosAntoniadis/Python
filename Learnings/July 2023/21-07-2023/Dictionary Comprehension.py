# dictionary comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions
#
# dictionary = {key: (if/else) OR function(value) "expression" for "(key, value)" in "iterable" -if conditional-}

Temperature = {"Netherlands": 25, "Greece": 45, "Norway": 19, "South Africa": 9}

TempF = {key: ((value*1.8000)+32) for (key, value) in Temperature.items()}
print(TempF)

print("---------------------------------------------------------------------------------")

weather = {"Netherlands": "raining", "Greece": "sunny", "Norway": "raining", "South Africa": "cloudy"}

WeaSunny = {key: value for (key, value) in weather.items() if value == "raining"}
print(WeaSunny)

print("---------------------------------------------------------------------------------")

Temperature = {"Netherlands": 25, "Greece": 45, "Norway": 19, "South Africa": 9}
Feeling_Temp = {key: ("COLD" if value <= 15 else "WARM") for (key, value) in Temperature.items()}
print(Feeling_Temp)

print("---------------------------------------------------------------------------------")


def check(value):
    if value <= 15:
        return "COLD"
    elif value > 15 and value <= 35:
        return "OK"
    else:
        return "HEAT WAVE"


Feeling_Temp2 = {key: check(value) for (key, value) in Temperature.items()}
print(Feeling_Temp2)

# 21/07/23