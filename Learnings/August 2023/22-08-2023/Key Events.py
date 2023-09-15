# window.bind(event, function)

from tkinter import *


def DoSomething(event):
    print("You pressed: " + event.keysym.upper())
    label.config(text=event.keysym.upper())


window = Tk()

window.bind("<Key>", DoSomething)

label = Label(window, font=("Helvetica", 80))
label.pack()


window.mainloop()

# 22/08/23