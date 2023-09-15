# Button = You click it, it does stuff

from tkinter import *

# Make a Counter
count = 0


def click():
    global count
    count+=1
    print(count)


window = Tk()

image = PhotoImage(file='Buttons Image.png')

button = Button(window,
                # the "master", the "container"
                text="Greece!",
                # text
                command=click,
                # the "callback", button's reply
                font=("Arial", 20, "bold"),
                # the font
                fg="Blue",
                # fg = foreground = text's/font's color (can use hex)
                bg="White",
                # bg = background = background color
                activeforeground="Blue",
                # command so font color doesn't change when clicking
                activebackground="White",
                # command so background color doesn't change when clicking
                state=ACTIVE,
                # when 'state=DISABLED', button doesn't work
                image=image,
                # import an image
                compound='bottom',
                # place the image on a specific place
                )

button.pack()


window.mainloop()

# 29/07/23