from tkinter import *


def createwindow():
    new_window = Tk()
    # or = Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    # if we close 'bottom' window, 'top' window also closes
    # Tk = Independent window.

    window.destroy()


window = Tk()

button = Button(window, text="Click Here", command=createwindow)
button.pack()


window.mainloop()

# 15/08/23