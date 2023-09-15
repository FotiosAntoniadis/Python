from tkinter import *
from tkinter import messagebox
#import message box


def click():
    messagebox.showinfo(title="Info Message Box", message="Never Gonna Give You Up!")

    # show info
    #------------------------------------------------------------------------------------------------
    #while(True):
        #messagebox.showwarning(title="WARNING!", message="Don't forget to drink your water!")

    # show warning (if 'while(True):', when click the OK, the window re-appears)
    #------------------------------------------------------------------------------------------------
    #messagebox.showerror(title="ERROR!", message="Something went wrong.")

    # show error
    #------------------------------------------------------------------------------------------------
    #if messagebox.askokcancel(title="Proceed", message="Do you want to proceed?"):
        #print("You destroyed your computer in your way to proceed.")
    #else:
        #print("You did not proceed. Have a nice day!")

    # Ok/Cancel Window
    #------------------------------------------------------------------------------------------------
    #if messagebox.askretrycancel(title="Retry", message="Do you want to retry?"):
        #print("You retried but it doesn't work")
    #else:
        #print("Ok, your choice. Have a nice day!")

    # Retry/Cancel Window
    #-----------------------------------------------------------------------------------------------
    #if messagebox.askyesno(title="Physique", message="Do you Exersise?"):
        #print("Good you Do!")
    #else:
        #print("You should try! It has many benefits.")

    # Yes/No Window (Returns Boolean Value: True/False)
    #-----------------------------------------------------------------------------------------------
    #answer = messagebox.askquestion(title="Question", message="Do you like Meditation?")

    #if answer == "yes":
        #print("Nice. I bet you are a responsible person!")
    #else:
        #print("You should start! Focus is an indicator of success!")

    # Yes/No Window (Returns Strings: "yes" or "no")
    #-----------------------------------------------------------------------------------------------
    #answer = messagebox.askyesnocancel(title="Block", message="Do you want to block this domain?")
    #if (answer == True):
        #print("The Blocking of this domain was Successful.")
    #elif (answer == False):
        #print("Ok. Probably a Miss-Click.")
    #else:
        #print("You chose to cancel this process.")

    # Yes/No/Cancel Window (Returns Values: True, False and None)


window = Tk()

button = Button(window, command=click, text="Click Here")
button.pack()


window.mainloop()

# Use 'icon={Winndow Type} to change the window's icon and theme.

# 05/08/23