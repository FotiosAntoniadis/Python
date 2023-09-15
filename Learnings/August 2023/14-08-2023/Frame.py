# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="Black",bd=5, relief=RAISED)
frame.pack()

buttonW = Button(frame, text="W", font=("Consolas", 25), width=3)
buttonW.pack(side=TOP)

buttonA = Button(frame, text="A", font=("Consolas", 25), width=3)
buttonA.pack(side=LEFT)

buttonS = Button(frame, text="S", font=("Consolas", 25), width=3)
buttonS.pack(side=LEFT)

buttonD = Button(frame, text="D", font=("Consolas", 25), width=3)
buttonD.pack(side=LEFT)


window.mainloop()

# 14/08/23