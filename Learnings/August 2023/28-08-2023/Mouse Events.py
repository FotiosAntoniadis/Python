from tkinter import *


def LeftClick(event):
    print("You Right-Clicked")


def RightClick(event):
    print("You Left-Clicked")


def ScrollWheel(event):
    print("You clicked the Scroll Wheel")


def Coordinates(event):
    print("Mouse Coordinates: " + str(event.x) + "," + str(event.y))


def Release(event):
    print("You let go the click")


def Enter(event):
    print("You entered the window")


def Leave(event):
    print("You left the window")


window = Tk()

window.bind("<Button-1>", LeftClick)
window.bind("<Button-2>", ScrollWheel)
window.bind("<Button-3>", RightClick)

window.bind("<Button-1>", Coordinates)

window.bind("<ButtonRelease>", Release)

window.bind("<Enter>", Enter)

window.bind("<Leave>", Leave)

window.bind("<Motion>", Coordinates)


window.mainloop()

# 28/08/23