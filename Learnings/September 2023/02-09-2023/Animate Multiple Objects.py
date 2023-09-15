from tkinter import *
import time
from Animate_Multiple_Objects_Classes_Modules import *


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "Yellow")
tennis_ball = Ball(canvas, 0, 0, 50, 3, 4, "Green")
basket_ball = Ball(canvas, 0, 0, 125, 8, 7, "Orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()

# 02/09/23