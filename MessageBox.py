from tkinter import *
from tkinter import messagebox

window = Tk()


def click():
    # messagebox.showinfo(title="Info Message", message="You are a person")
    # messagebox.showwarning(title="Warning", message="You have a virus")
    # messagebox.showerror(title="Error!", message="Something went wrong!")

    """if messagebox.askokcancel(title="Ask okay Cancel", message="Do you want to do the thing?") :
        print("You did a thing!")
    else:
        print("You canceled a thing")"""

    """if messagebox.askretrycancel(title="Ask okay Cancel", message="Do you want to do the thing?") :
        print("You retried a thing!")
    else:
        print("You canceled a thing")"""

    """if messagebox.askyesno(title="Ask yes or no", message="Do you like cake?"):
        print("I like cake too")
    else:
        print("Why do you not like cake?")"""

    """answer = messagebox.askquestion(title="Ask questions", message="Do you like pie?")
    if answer == 'yes':
        print("I like pie too")
    else:
        print("Why do you not like pie")"""

    answer = messagebox.askyesnocancel(title="Yes, No, Cancel", message="Do you like to code?")
    if answer == True:
        print("You like to code")
    elif answer == False:
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodge the question")


button = Button(window, command=click, text='Click Me')
button.pack()

window.mainloop()
