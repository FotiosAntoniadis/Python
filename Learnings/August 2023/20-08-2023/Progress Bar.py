from tkinter import *
from tkinter.ttk import *
import time


def download():
    tasks = 10
    x = 0
    while (x < tasks):
        time.sleep(1)
        bar['value'] += 10
        # ^^^ command so every time we click on the button, the bar gets filled by 10% (10/100) (if alone)
        x += 1
        percent.set(str(int((x/tasks)*100)) + "%")
        task.set(str(x) + "/" + str(tasks) + " tasks completed")
        window.update_idletasks()



window = Tk()

percent = StringVar()
task = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack()

PercentLabel = Label(window, textvariable=percent)
PercentLabel.pack()

TaskLabel = Label(window, textvariable=task)
TaskLabel.pack()

button = Button(window, text="Download", command=download)
button.pack()

window.mainloop()

# 20/08/23