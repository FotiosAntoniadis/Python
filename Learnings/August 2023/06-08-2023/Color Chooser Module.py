from tkinter import *
from tkinter import colorchooser
#submodule


def click():
    color = colorchooser.askcolor()
    print(color)
    color_hex = color[1]
    print(color_hex)
    window.config(bg=color_hex)

    # change background color


window = Tk()

window.geometry("420x420")

button = Button(window, text="Click Here", command=click)
button.pack()


window.mainloop()

# 06/08/23