# canvas = widget that is udes to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)

canvas.create_line(0, 0, 500, 500, fill="Blue", width=5)

canvas.create_line(0, 500, 500, 0, fill="Red", width=5)

canvas.create_rectangle(50, 50, 250, 250, fill="Green")

canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="Yellow", outline="Black", width=5)
# OR
points = [0, 0, 250, 500, 500, 0]
canvas.create_polygon(points, fill="Purple", outline="Black", width=5)

canvas.create_arc(0, 0, 500, 500, fill="Brown", style=ARC, start=90, extent=180)
# arc is a curved line bettween 2 points
# style = ARC = curved line, style = CHORD = Bow, Χορδή
# start = [DEGREES] = rotate the shape by degrees
# extent = [DEGREES] = The angle that should be created

canvas.create_oval(190, 190, 310, 310, fill="Orange")
# create oval = circle

canvas.pack()


window.mainloop()

# 21/08/23