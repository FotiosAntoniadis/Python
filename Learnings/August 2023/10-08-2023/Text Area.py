# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *


def submit():
    typing = (text.get("1.0", END))
    print(typing)


window = Tk()

text = Text(window,
            # the "master", the container
            bg="Light Yellow",
            # bg = background = background color
            font=("Arial", 20),
            # the font
            height=8,
            width=20,
            # when you change the font's size, the window's size also changes, so it coresponds. So you need to resize.
            padx=20,
            # space (in pixels) between text and window border(Horizontally)
            pady=20,
            # space (in pixels) between text and window border(Vertically)
            fg="Black"
            # fg = foreground = font color
            )
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()


window.mainloop()

# 10/08/23