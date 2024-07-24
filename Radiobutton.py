from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text= food[index],  # adds text to radio buttons
                              var= x,  # groups radiobutton together if they share the same variable
                              value= index, # assigns each radiobutton a different value
                              padx= 25,
                              font=("Impact", 20)
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
