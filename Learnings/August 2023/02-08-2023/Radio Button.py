# Radio Button = Similar to Checkbox, but you can only select one from a group

from tkinter import *

operating_system = ["Windows", "Apple", "Linux"]


def choose():
    if (x.get() == 0):
        # x = variable = IntVar = 0,1,2
        print("You chose: Windows")
    elif (x.get() == 1):
        print("You chose: Apple")
    elif (x.get() == 2):
        print("You chose: Linux")
    else:
        print("Huh?")


window = Tk()

Linux = PhotoImage(file='Radio Button Image Linux.png')
Apple = PhotoImage(file='Radio Button Image Apple.png')
Windows = PhotoImage(file='Radio Button Image Windows.png')
# convert images to 'PhotoImage' form.

OP_Images = [Windows, Apple, Linux]
# create a list with the images

x = IntVar()

for i in range(len(operating_system)):
    radio_button = Radiobutton(window,
                               # the "master", the container
                               text=operating_system[i],
                               # text
                               variable=x,
                               # groups radiobuttons together if they share the same variable
                               value=i,
                               # assigns each radiobutton a different value
                               padx=20,
                               # space (in pixels) between text and border(Horizontally)
                               font=("Arial", 15),
                               # the font
                               image=OP_Images[i],
                               # input images
                               compound='left',
                               # place the images on a specific place
                               indicatoron=0,
                               # eliminate circles, radiobutton turn into push-buttons
                               width=300,
                               # change the width of the push-buttons
                               command=choose)

    radio_button.pack(anchor=W,
                      # command so the radiobuttons allign
                      )

window.mainloop()

# 02/08/23