from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves a container to hold or contain these widgets

window = Tk()
# instantiate an instance of a window

window.geometry("420x420")
# change window's measurements

window.title("Deez Window")
# change window's name

icon = PhotoImage(file='Graphical User Interface Image.png')
# change icon from png (can't input) to Photo Image (can input) (jpg cannot be recognised)

window.iconphoto(True, icon)
# put "icon" as window icon/logo

window.config(background="black")
# change window's background color (can use hex, if you want)

window.mainloop()
# display window

# 27/07/23