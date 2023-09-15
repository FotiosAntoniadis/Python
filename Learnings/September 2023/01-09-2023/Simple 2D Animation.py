from tkinter import *
import time

WIDTH = 1119
HEIGHT = 790

xVelocity = 2
yVelocity = 3

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background = PhotoImage(file='Simple 2D Animation Image Stadium.png')
stadium = canvas.create_image(0, 0, image=background, anchor=NW)

image = PhotoImage(file='Simple 2D Animation Image Ball.png')
ball = canvas.create_image(0, 0, image=image, anchor=NW)

image_width = image.width()
image_height = image.height()

while True:
    coordinates = canvas.coords(ball)
    print(coordinates)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()

# 01/09/23 Code Doesn't Work