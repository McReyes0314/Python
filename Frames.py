from tkinter import *

window = Tk()
window.geometry("300x300")
label_text = StringVar()
label_text.set("You did not press anything yet")


def press_w():
    label_text.set("You Press W")


def press_a():
    label_text.set("You Press A")


def press_s():
    label_text.set("You Press S")


def press_d():
    label_text.set("You Press D")


def reset():
    label_text.set("You did not press anything yet")


label = Label(window,
              textvariable=label_text,
              font=("Arial", 10),
              pady=30)
label.pack(side=TOP)

frame = Frame(window, bg="pink")
frame.pack()
# frame.place(x=0, y=0)

w_button = Button(frame, text="W", font=("Consolas", 25),width=3, command=press_w,)
w_button.pack(side=TOP)

a_button = Button(frame, text="A", font=("Consolas", 25), width=3, command=press_a)
a_button.pack(side=LEFT)

a_button = Button(frame, text="S", font=("Consolas", 25), width=3, command=press_s)
a_button.pack(side=LEFT)

d_button = Button(frame, text="D", font=("Consolas", 25), width=3, command=press_d)
d_button.pack(side=LEFT)

reset_button = Button(text="Reset", font=("Consolas", 15), width=6, command=reset)
reset_button.pack(side=BOTTOM)

window.mainloop()