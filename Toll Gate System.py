from tkinter import *
from tkinter import messagebox


window = Tk()

# window
window.title("Toll Gate System")
window.geometry("300x300")

# variable
totalVeh = 0
totalAmnt = 0


# commands
def entry():
    global totalVeh
    global totalAmnt
    totalVeh += 1
    totalAmnt += 10
    totalVehicle.config(text=f"Total Vehicle: {totalVeh}")
    totalAmount.config(text=f"Total Amount: {totalAmnt}")


def exit():
    global totalVeh
    if totalVeh > 0:
        totalVeh -= 1
        totalVehicle.config(text=f"Total Vehicle: {totalVeh}")
    else:
        messagebox.showwarning("Total Vehicle", "There is no vehicle to exit now")


# label
titleLabel = Label(window, text="Toll Gate System", font=("Times New Roman", 20))
titleLabel.place(x=50, y=20)

frame = Frame(window)
frame.place(x=50, y=80)

totalVehicle = Label(frame, text=f"Total Vehicle: {totalVeh}", font=("Arial", 15))
totalVehicle.pack(pady=0)

totalAmount = Label(frame, text=f"Total Amount: {totalAmnt}", font=("Arial", 15))
totalAmount.pack(pady=20)

# buttons
VehicleEntry = Button(window, text="Vehicle Entry", fg="white", bg="Maroon", font=("Arial", 10), width=15, command=entry)
VehicleEntry.place(x=115, y=180)

VehicleEntry = Button(window, text="Vehicle Exit", fg="white", bg="Maroon", font=("Arial", 10), width=15, command=exit)
VehicleEntry.place(x=115, y=220)

window.mainloop()