# For Loop = a statement that will execute its block of code a limited amount of times

# While Loop = Unlimited
# For Loop = Limited

for i in range(10):
    print(i+1)

#---------------------------------------------------------------
print("------------------------------------------------------------")
#---------------------------------------------------------------


for i in range(50, 100, 2):
    #          ^    ^   ^
    #        start,end,skip
    print(i+1)

#---------------------------------------------------------------
print("------------------------------------------------------------")
#---------------------------------------------------------------

for i in "Deez Nuts":
    print(i)

#---------------------------------------------------------------
print("------------------------------------------------------------")
#---------------------------------------------------------------

import time

for seconds in range(10,0,-1):
    #                ^  ^  ^
    #            start,end,way of calculation
    print(seconds)
    time.sleep(1)
print("Deez!")

#24/06/23