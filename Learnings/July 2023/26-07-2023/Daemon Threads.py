# Daemon Threads = threads that run in the backround, not important for program to run
# Your Program will not wait for Daemon Threads to complete before exit-ing.
# (Daemon Thread is killed when it has not done its task, but main thread has completed its)
# non-Daemon threads cannot be normally killed, stay alive until task is complete
#
# ex. background tasks, garbage collection, waiting for input, long-running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: " + str(count) + " seconds.")


x = threading.Thread(target=timer, daemon=True)
x.start()

# Change a thread to a daemon one or a normal one:
# x.setDaemon(True)

# See if thread is daemon type:
# print(x.isDaemon())

answer = input("Do you wish to exit? ")

# 26/07/23