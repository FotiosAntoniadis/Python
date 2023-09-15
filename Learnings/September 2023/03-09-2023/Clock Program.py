from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    window.after(1000, update)
    #                  ^         ^
#   in miliseconds 1000 = 1 sec /Call agian the function, repeat process of updating window


window = Tk()

time_label = Label(window, font=("Arial", 30), fg="Black", bg="White")
time_label.pack()

day_label = Label(window, font=("Arial", 10), fg="Black", bg="White")
day_label.pack()

date_label = Label(window, font=("Arial", 10), fg="Black", bg="White")
date_label.pack()

update()


window.mainloop()

# 03/09/23