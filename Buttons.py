from tkinter import *

# buttons = you click it, then it does stuff
window = Tk()

count = 0


def click():
    global count
    count += 1
    print(count)


button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="Green",
                bg="Black",
                activebackground="Black",
                activeforeground="Green"
                # state=DISABLED
                )

button.pack()

window.mainloop()
