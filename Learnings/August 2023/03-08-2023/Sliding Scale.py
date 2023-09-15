from tkinter import *


def submit():
    print("You are " + str(scale.get()) + " years old.")


window = Tk()

Kids = PhotoImage(file='Sliding Scale Image Kids.png')
KidsLabel = Label(image=Kids)
KidsLabel.pack()

scale = Scale(window,
              # the "master", the container
              from_=0,
              # starting point(upper/left)
              to=100,
              # ending point(lower/right)
              length=600,
              # the length of the scale
              orient=VERTICAL,
              # direction/orientation of the scale
              font=("Arial", 15),
              # the font
              tickinterval=10,
              # numeric scale/indicators next to the scale
              #showvalue=0,
              # hide current value
              #resolution=5,
              # comand so the current value clips up to numbers that are multiples of 5
              troughcolor="Black",
              # change scale's color
              fg="Black",
              # fg = foreground = font color
              bg="White",
              # bg = background = background color
              )

scale.set(14)
# change default position of the current value

#scale.set(((scale['from']-scale[to])/2)+scale['to'])
# formula so the current-value's default position is always on the middle

scale.pack()

Elders = PhotoImage(file='Sliding Scale Image Elders.png')
EldersLabel = Label(image=Elders)
EldersLabel.pack()

button = Button(window, text="Submit", command=submit)
button.pack()


window.mainloop()

# 03/08/23