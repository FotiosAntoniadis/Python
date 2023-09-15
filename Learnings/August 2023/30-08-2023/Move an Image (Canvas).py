from tkinter import *


def MoveUp(event):
    canvas.move(image, 0, -10)


def MoveLeft(event):
    canvas.move(image, -10, 0)


def MoveDown(event):
    canvas.move(image, 0, +10)


def MoveRight(event):
    canvas.move(image, +10, 0)


window = Tk()

window.bind("<w>", MoveUp)
window.bind("<a>", MoveLeft)
window.bind("<s>", MoveDown)
window.bind("<d>", MoveRight)

window.bind("<Up>", MoveUp)
window.bind("<Left>", MoveLeft)
window.bind("<Down>", MoveDown)
window.bind("<Right>", MoveRight)

canvas = Canvas(window,  height=500, width=500)
canvas.pack()

photoimg = PhotoImage(file="Move_an_Image_Image.png")
image = canvas.create_image(0, 0, image=photoimg, anchor=NW)


window.mainloop()

# 30/08/23