from tkinter import *
from tkinter import messagebox


def addEmployee():
    nam = name.get()
    pos = position.get()
    sal = salary.get()

    newEmployee = [nam, pos, sal]
    employeeList.append(newEmployee)

    messagebox.showinfo("Add Employee", "Employee is been added")


def viewEmployee():
    newWindow = Toplevel(window)
    newWindow.title("View Employee")
    newWindow.geometry("410x300")

    viewText = Text(newWindow)
    viewText.pack(expand=True, fill=BOTH)
    viewText.insert(END, f"Name\t\tPosition\t\tSalary\n")
    viewText.insert(END, "-" * 50 + "\n")

    for b in employeeList:
        viewText.insert(END, f"{b[0]}\t\t{b[1]}\t\t{b[2]}")


def clear():
    name.delete(0, END)
    position.delete(0, END)
    salary.delete(0, END)


window = Tk()

window.geometry("300x300")
labelTitle = Label(text="Employee Salary System", font=("Times New Roman", 20), fg="Maroon")
labelTitle.place(x=15, y=20)

fields = Frame(window)
fields.place(x=15, y=80)

employeeList = []

# name
nameLabel = Label(fields, text="Name: ", font=("Arial", 12), pady=5)
nameLabel.grid(row=0, column=0)
name = Entry(fields, font=("Arial", 12))
name.grid(row=0, column=1)

# position
positionLabel = Label(fields, text="Position: ", font=("Arial", 12), pady=5)
positionLabel.grid(row=2, column=0)
position = Entry(fields, font=("Arial", 12))
position.grid(row=2, column=1)

# salary
salaryLabel = Label(fields, text="Salary: ", font=("Arial", 12), pady=5)
salaryLabel.grid(row=3, column=0)
salary = Entry(fields, font=("Arial", 12))
salary.grid(row=3, column=1)

# add button
addButton = Button(window, text="Add Employee", command=addEmployee, width=15, bg="Maroon", fg="White")
addButton.place(x=160, y=200)

# view Button
viewButton = Button(window, text="View Employee", command=viewEmployee, width=15, bg="Maroon", fg="White")
viewButton.place(x=160, y=230)

# clear Button
clearButton = Button(window, text="Clear", command=clear, width=15, bg="Maroon", fg="White")
clearButton.place(x=160, y=260)

window.mainloop()