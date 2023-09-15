from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askeditfile(title="Open a File",
                                          # change window's name
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*"))
                                          # give options to the user to search for certain types of files
                                          )
    file = open(filepath, 'r')
    print(file.read())
    file.close()
    print("File has been opened!")


def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

    print("File has been saved!")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("You pasted some text!")


window = Tk()

openimage = PhotoImage(file="Menu Bar Image Folder.png")
saveimage = PhotoImage(file="Menu Bar Image Disk.png")
exitimage = PhotoImage(file="Menu Bar Image X.png")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=openfile, image=openimage, compound="left")
filemenu.add_command(label="Save", command=savefile, image=saveimage, compound="left")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit, image=exitimage, compound="left")

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)


text = Text(window)
text.pack()


window.mainloop()

# 13/08/23