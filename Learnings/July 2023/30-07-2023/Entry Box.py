# Entry Widget = Textbox that accepts a single line of user input

from tkinter import *


def submit():
    username = entry.get()
    print("Hello " + username + ".")


# Function that disables the usage/purpose of the window after entering the text
#entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              # the "master", the container
              font=("Arial", 20),
              # the font
              fg="Black",
              # fg = foreground = font color
              bg="White",
              # bg = background = background color
              #show="*"
              # useful for passwords, when typing, shows only a certain character.
              )

# Input some text in a defined place
#entry.insert(0, "Enter Username: ")

entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

submit_button = Button(window, text="Delete", command=delete)
submit_button.pack(side=RIGHT)

submit_button = Button(window, text="Backspace", command=backspace)
submit_button.pack(side=RIGHT)


window.mainloop()

# 30/07/23