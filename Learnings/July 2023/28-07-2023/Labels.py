# Label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file="Labels Image.png")

# Create the label
label = Label(window,
              # the container
              text="Zyzz",
              # text
              font=("Arial", 18, "bold"),
              # font
              fg="Black",
              # foreground = font color
              bg="White",
              # background color
              relief=RAISED,
              # label border
              bd=10,
              # border's thickness
              padx=20,
              # space (in pixels) between text and border(Horizontally)
              pady=20,
              # space (in pixels) between text and border(Vertically)
              image=photo,
              # input an image
              compound="bottom",
              # place the image in a cordinated place
              )

# Input the label
label.pack()

# Place the label in a cordinated place
#label.place(x=100, y=100)


window.mainloop()

# 28/07/23