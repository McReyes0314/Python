from tkinter import *

window = Tk()

f

w_button = Button(text="W", font=("Consolas", 25),width=3)
w_button.pack(side=TOP)

a_button = Button(text="A", font=("Consolas", 25), width=3)
a_button.pack(side=LEFT)

a_button = Button(text="S", font=("Consolas", 25), width=3)
a_button.pack(side=LEFT)

d_button = Button(text="D", font=("Consolas", 25), width=3)
d_button.pack(side=LEFT)

window.mainloop()