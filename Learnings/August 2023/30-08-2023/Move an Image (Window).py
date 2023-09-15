from tkinter import *


def MoveUp(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)


def MoveLeft(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def MoveDown(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def MoveRight(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())




window = Tk()

window.bind("<w>", MoveUp)
window.bind("<a>", MoveLeft)
window.bind("<s>", MoveDown)
window.bind("<d>", MoveRight)

window.bind("<Up>", MoveUp)
window.bind("<Left>", MoveLeft)
window.bind("<Down>", MoveDown)
window.bind("<Right>", MoveRight)

image = PhotoImage(file="Move_an_Image_Image.png")

window.geometry("500x500")

label = Label(window, image=image)
label.place(x=0, y=0)


window.mainloop()

# 30/08/23