from tkinter import *


def doSomething(event):
    label.config(text="You Pressed: "+event.keysym)


window = Tk()
window.geometry("300x300")
window.bind("<Key>", doSomething)

label = Label(window, font=("Helvetica", 20))
label.pack()

window.mainloop()