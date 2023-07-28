import time

# Find out the computer's epoch (when your computer thinks time began)
print(time.ctime(0))

# Find how many seconds passed from epoch
print(time.time())

# Find out what date is today
print(time.ctime(time.time()))

# Find with more accuracy
time_object = time.localtime()
print(time_object)

# String Format time (See Python's documentation)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

# UTC (Coordinated Universal Time)
utc = time.gmtime()

# String representing time
timestring = "24 July, 2023"
stringtime = time.strptime(timestring, "%d %B, %Y")
print(stringtime)

# Tuple representing time (The last are 0s, because thy don't count, for now)
# (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_tuple = (2023, 7, 24, 13, 28, 0, 0, 0, 0)
time_str = time.asctime(time_tuple)
print(time_str)
# OR (since epoch, below)
time_tuple = (2023, 7, 24, 13, 28, 0, 0, 0, 0)
time_str2 = time.mktime(time_tuple)
print(time_str2)

# 24/07/23