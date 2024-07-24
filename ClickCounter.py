"""
Features:
- A button that increments a counter each time it is clicked.
- A display that show the current count.
"""
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")

counter = 0


def count():
    global counter
    counter += 1
    counter_label = Label(window, text=f"count: {counter}", font=('Arial', 15))
    counter_label.place(x=65, y=0)

def reset():
    global counter
    counter = 0
    counter_label = Label(window, text=f"count: {counter}", font=('Arial', 15), width=20)
    counter_label.place(x=65, y=0)





countButton = Button(window, text="Count", font=("Arial", 10), width=20, command=count)
countButton.place(x=65, y=60)
resetButton = Button(window, text="Reset", font=("Arial", 10), width=20, command=reset)
resetButton.place(x=65, y=120)
exitButton = Button(window, text="Exit", command=quit, font=("Arial", 10), width=20)
exitButton.place(x=65, y=180)
window.mainloop()
