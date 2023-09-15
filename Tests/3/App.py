from tkinter import *

from tkinter import messagebox

if ModuleNotFoundError:
    messagebox.askokcancel(title="Error.", message="First Open 3.exe to Create an Account, so the code runs efficiently", icon="error")
else:
    pass

from log import *


if Gender == '0':
    Gender = "Male"
else:
    Gender = "Female"

if Notifications == '1':
    Notifications = "ON"
else:
    Notifications = "OFF"


window = Tk()

label1 = Label(text=("Hello " + Username), font=("Arial", 35))
label1.pack()

label2 = Label(text="Your information:", font=("Arial", 30))
label2.pack()

label3 = Label(text=("Gender: " + Gender), font=("Arial", 20))
label3.pack()

label4 = Label(text=("Age: " + Age), font=("Arial", 20))
label4.pack()

label5 = Label(text=("Interests: " + Interests), font=("Arial", 20))
label5.pack()

label6 = Label(text=("Notifications: " + Notifications), font=("Arial", 20))
label6.pack()

window.mainloop()