# ListBox = A listing of selectable text items within its own container

from tkinter import *


def submit():

    interests = []

    for i in listbox.curselection():
        interests.insert(i, listbox.get(i))

    print("Your interest/s in improvement is/are: ")

    for i in interests:
        print(i)


def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())


def delete():

    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())



window = Tk()

listbox = Listbox(window,
                  # the "master", the container
                  bg="White",
                  # bg = background = background color
                  font=("Arial", 20),
                  # the font
                  width=12,
                  # the width of the window
                  selectmode=MULTIPLE
                  # command so that we can choose more than 1 value
                  )
listbox.pack()

listbox.insert(1, "Reading")
listbox.insert(2, "Awareness")
listbox.insert(3, "Wellbeing")
listbox.insert(4, "Exercise")
listbox.insert(5, "Gratitude")


listbox.config(height=listbox.size())
# command so the window adjusts automatically

entrybox = Entry(window)
entrybox.pack()


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()



window.mainloop()

# 04/08/23