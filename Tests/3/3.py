from tkinter import *
from tkinter import messagebox
import os
import shutil

if ModuleNotFoundError:
    messagebox.askokcancel(title="Error.",
                           message="First Open Install.exe to Install",
                           icon="error")
else:
    pass

from perm import *


genders = ["Male", "Female"]


def notifs():
    if (x.get() == 1):
        print("You enabled Notifications.")
    else:
        print("You disabled Notifications.")


def submit():
    if messagebox.askokcancel(title="Account Creation", message='By clicking "Ok", you will create an account ',
                              icon="info"):
        info = "Username = '" + username.get() + "'\nGender = '" + str(y.get()) + "'\nAge = '" + str(age.get()) + "'\nInterests = '" + str(interests.curselection()) + "'\nNotifications = '" + str(x.get()) + "'"
        with open("log.py", "w") as file:
            file.write(info)

        iw = "App.exe"
        os.system(iw)

        path = "3.exe"
        os.remove(path)

        path2 = "perm.py"
        os.remove(path2)


        window.destroy()


window = Tk()

sourceInfoApp = "App.py"
destinationInfoApp = "C:\\Users\\Kosma\\PycharmProjects\\3\\App.py"

distfolder = "dist"
os.rmdir(distfolder)

# Here I will place code for deletion of useless folders and moving of useful files to the main folder.

window.title("Create Account")

icon = PhotoImage(file='C:\\Users\\Kosma\\PycharmProjects\\3\\3_Image.png')

window.iconphoto(True, icon)

x = IntVar()

y = IntVar()

window.geometry("500x620")

interface1 = Label(window, text="Create Account", font=("Arial", 15))
interface1.pack()

interface1Part2 = Label(window, text="‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾", font=("Arial", 10))
interface1Part2.pack()

interface2 = Label(window, text="Please Enter a username:", font=("Arial", 10))
interface2.pack()

username = Entry(window)
username.pack()

interface2Part2 = Label(window, text=" ", font=("Arial", 10))
interface2Part2.pack()

interface3 = Label(window, text="What's your Gender?", font=("Arial", 10))
interface3.pack()

for i in range(len(genders)):
    gender = Radiobutton(window, text=genders[i], variable=y, value=i)
    gender.pack()

interface3Part2 = Label(window, text=" ", font=("Arial", 10))
interface3Part2.pack()

interface4 = Label(window, text="What's your Age?", font=("Arial", 10))
interface4.pack()

age = Scale(window, from_=0, to=100, length=200, orient=HORIZONTAL, tickinterval=25)
age.pack()

interface4Part2 = Label(window, text=" ", font=("Arial", 10))
interface4Part2.pack()

interface5 = Label(window, text="Choose some pre-installed interests in improvement:", font=("Arial", 10))
interface5.pack()

interests = Listbox(window, selectmode=MULTIPLE)
interests.pack()

interests.insert(1, "Knowledge & Mindset")
interests.insert(2, "Physique")
interests.insert(3, "Awareness")
interests.insert(4, "Gratitude")
interests.insert(5, "Business & Money")
interests.insert(6, "Relationships")
interests.insert(7, "Stoicism")
interests.insert(8, "Leadership")

interests.config(height=interests.size())

interface5Part2 = Label(window, text=" ", font=("Arial", 10))
interface5Part2.pack()

notifications = Checkbutton(window, text="Send me Notifications", variable=x, onvalue=1, offvalue=0, command=notifs)
notifications.pack()

interface6 = Label(window, text=" ", font=("Arial", 10))
interface6.pack()

submit = Button(window, text="Create Account", font=("Arial", 10), fg="Black", command=submit)
submit.pack()

window.mainloop()

# 06/08/23 Basic stuff done. Sceleton done, need to make it beautiful and learn how to store data.
# 07/08/23 Design Done. I like it simple.
# 08/08/23 Changed some settings, designed the outer window. Need to use if statements for blocking.

# 09/08/23
# I can make separated windows that will use the window.destroy() function to close previous windows when a new opens
# This way, I can use print() to interact with the user, due to buttons with functions!

# 07/09/23 Make log show male(y.get() == 0), female(y.get() == 1), notifs on(x.get() == 1) and
# notifs off(x.get() == 0). Interests don't bother.

# 08/09/23 App.py ready. Need to program custom destinations (need to learn) and make the .py files to .exe
# files. Also need to program delete commands for .idea and venv. I'm thinking of moving all (useful,
# remaining) files to main folder after deletion of useless files.

# 09/09/23 Done some troubleshooting. Need to learn how to custom directions, so it binds in every computer.