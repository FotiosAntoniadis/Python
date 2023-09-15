from tkinter import *
from tkinter import ttk


window = Tk()

notebook = ttk.Notebook(window)
# Widget that manages a collection of windows/displays

Tab1 = Frame(notebook)
# New frame for Tab1

Tab2 = Frame(notebook)
# New frame for Tab2

notebook.add(Tab1, text="Tab1")
notebook.add(Tab2, text="Tab2")

notebook.pack(expand=True, fill="both")
# Expand = expand to fill any space not otherwise used
# Fill = fill space on x and y axis

Label(Tab1, text="This is Tab1. This tab is boring. If you want to find out Interesting Things, check out Tab2",
      width=50, height=25).pack()
Label(Tab2, text="This is Tab2. Here you can find out Interesting Things",
      width=50, height=25).pack()

window.mainloop()

# 17/08/23