# grid = geometry manager that organizes widgets in a table-like structure in a parent window/container

from tkinter import *


def submit():
    print("Your information was submited")
    print("Your name is: " + str(FirstNameEntry.get()) + " " + str(LastNameEntry.get() + "."))
    print("A 6 digit number has been sent to your inbox(" + str(EmailEntry.get()) + ")")


window = Tk()

TitleLabel = Label(window, text="Enter your information:", font=("Arial", 15))
TitleLabel.grid(row=0, column=0, columnspan=2)

FirstNameLabel = Label(window, text="First Name: ")
FirstNameLabel.grid(row=1, column=0)

FirstNameEntry = Entry(window)
FirstNameEntry.grid(row=1, column=1)


LastNameLabel = Label(window, text="Last Name: ")
LastNameLabel.grid(row=2, column=0)

LastNameEntry = Entry(window)
LastNameEntry.grid(row=2, column=1)


EmailLabel = Label(window, text="Email: ")
EmailLabel.grid(row=3, column=0)

EmailEntry = Entry(window)
EmailEntry.grid(row=3, column=1)

SubmitButton = Button(window, text="Submit", command=submit)
SubmitButton.grid(row=4, column=0, columnspan=2)

window.mainloop()

# 19/08/23