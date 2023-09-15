from tkinter import *
from tkinter import messagebox
import os


def sbmt():
        source = "3"
        destination = direction.get() + "\\3"

        try:
            if os.path.exists(destination):
                messagebox.askokcancel(title="Install", text="There is already a folder in this directory")
            else:
                os.replace(source, destination)
                messagebox.askokcancel(title="Install", text="Installation Complete")

        except FileNotFoundError:
            messagebox.askokcancel(title="Install", text="Folder not Found / Program Crashed")

        p = "Done"
        with open("perm.py", "w") as file:
            file.write(p)

        path = "install.exe"
        os.remove(path)

        installW.destroy()



installW = Tk()

label = Label(installW, text="Enter a directory to start installing.", font=("Arial", 20))
label.pack()

direction = Entry(installW)
direction.pack()

label2 = Label(installW, text="directory = folder", font=("Arial", 10))
label2.pack()

button = Button(installW, text="Install", command="sbmt")
button.pack()

installW.mainloop()

# 10/09/23 Basic window done, make 3.py read perm.py and when log.py is created, both perm.py and 3.exe get deleted
# as for install.exe, I should make it delete itself when process-is-finished/perm.py-is-created.

# 11/09/23 Yesterday's stuff done