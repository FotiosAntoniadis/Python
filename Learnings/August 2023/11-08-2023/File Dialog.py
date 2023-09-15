from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(title="Open a File",
                                          # change window's name
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*"))
                                          # give options to the user to search for certain types of files
                                          )
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(window, text="Open", command=openfile)
button.pack()


window.mainloop()

# 11/08/23