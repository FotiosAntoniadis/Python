from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return
    # if statement, so error doesn't pop us when saving empty file

    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

    # we can use the console to save files, via the 'input' module


window = Tk()

button = Button(window, text="Save", command=savefile)
button.pack()

text = Text(window)
text.pack()


window.mainloop()

# 12/08/23