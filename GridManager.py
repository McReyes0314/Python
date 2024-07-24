from tkinter import *
from tkinter import messagebox

# grid() = geometry manager that organizes a window in a table-like structure in a parent

window = Tk()
window.geometry("200x200")
window.resizable = False


def confirm():
    messagebox.showinfo("Confirmation", message="Your info is save")


firstNameLabel = Label(window, text="First name: ", pady=15)
firstNameLabel.grid(row=0, column=0)
firstNameEntry = Entry(window)
firstNameEntry.grid(row=0, column=1)

lastNameLabel = Label(window, text="Last name: ", pady=15)
lastNameLabel.grid(row=1, column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row=1, column=1)

emailLabel = Label(window, text="Email", pady=15)
emailLabel.grid(row=2, column=0)
emailEntry = Entry(window)
emailEntry.grid(row=2, column=1)

button = Button(window, text="Submit", command=confirm)
button.grid(row=3, column=0, columnspan=2)
window.mainloop()
