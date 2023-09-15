from tkinter import*


def Drag_Start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def Drag_Motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


window = Tk()

label = Label(window, bg="Blue", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg="Red", width=10, height=5)
label2.place(x=100, y=100)

label.bind("<Button-1>", Drag_Start)
label.bind("<B1-Motion>", Drag_Motion)

label2.bind("<Button-1>", Drag_Start)
label2.bind("<B1-Motion>", Drag_Motion)


window.mainloop()

# 29/08/23