# thread = a flow of execution. Like a separate order of instructions.
# However, each tread takes a turn running to achieve concurrency
# GIL = global interpreter lock
# Allows only one thread to hold the control of the Python interpreter qat any one time

# CPU bound = program/task spends most of it's time waiting for internal events (CPU intensive)
# Use multiprocessing

# io(input/output) bound = program/task spends most of it's time waiting for external events (user input, web scraping)
# Use multithreading

import threading
import time

# 10 mins = 1 sec


def study():
    time.sleep(3)
    print("You studied.")


def check_bag():
    time.sleep(1)
    print("You checked your bag.")


def read_book():
    time.sleep(4)
    print("You read your book.")


x = threading.Thread(target=study(), args=())
x.start()

y = threading.Thread(target=check_bag(), args=())
y.start()

z = threading.Thread(target=read_book(), args=())
z.start()

# Function that tells to main thread what thread to wait before executing
x.join()
y.join()
z.join()

#study()
#check_bag()
#read_book()

# Active/Running threads rn
print(threading.active_count())

# List of Running threads
print(threading.enumerate())

# Time concumed by the main thread to complete its task
print(time.perf_counter())

# 25/07/23. This threading didn't work as expected. Maybe Python changed, or I'm an idiot. OR my it's computer
# fault. Most likely it's this.