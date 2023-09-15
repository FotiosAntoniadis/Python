from tkinter import *


def display():
    if(x.get() == 1):
        print("You agree.")
    else:
        print("You don't agree.")


window = Tk()

image = PhotoImage(file='Checkbox Image.png')

x = IntVar()
# if 'x = IntVar', every time we click on check button, checkbutton = 1 or 0
# if 'x = StringVar', every time we click on check button, checkbutton = str1 or str2
# if 'x = BooleanVar', every time we click on check button, checkbutton = True or False

check_button = Checkbutton(window,
                           # the "master", the container
                           text="I agree to something.",
                           # the text
                           variable=x,
                           # the responce
                           onvalue=1,
                           # if checkbutton clicked Odd number of times, then checkbutton = 1 / On
                           offvalue=0,
                           # if checkbutton clicked Even number of times, then checkbutton = 0 / Off
                           command=display,
                           # the function that will detect if checkbutton == 1 or 0
                           font=("Arial", 20, "bold"),
                           fg="Black",
                           # fg = foreground = font color
                           bg="White",
                           # bg = background = background color
                           activeforeground="Black",
                           # function so every time we click, the font doesn't flash / change color
                           activebackground="White",
                           # function so every time we click, the background doesn't flash / change color
                           padx=20,
                           # space (in pixels) between text and border(Horizontally)
                           pady=20,
                           # space (in pixels) between text and border(Vertically)
                           image=image,
                           # import an image
                           compound='left')


check_button.pack()

window.mainloop()

# 31/07/23