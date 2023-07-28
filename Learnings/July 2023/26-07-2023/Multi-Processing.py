# Multi-Processing = running tasks in parallel on different CPU cores, bypasses GIL used for threads
#
# Multi-Processing = Better for CPU bound tasks (heavy CPU usage)
# Multi-Threading = Better for IO bound tasks (waiting around, input/output)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))


    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

# Let's see how many seconds it took to my computer to count to 1000000000 OR 1000000000/2 OR 1000000000/4.
    print("Finished in:", time.perf_counter(), "seconds.")


# For windows operating system, so the child module gets copied but not executed
if __name__ == '__main__':
    main()

# 26/07/23