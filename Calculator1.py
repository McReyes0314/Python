from tkinter import *

def click_button(value):
    current = label.cget("text")
    if current == "0" or current == "ERROR":
        current = ""
    label.config(text=current + str(value))

def clear():
    label.config(text="0")

def calculate():
    try:
        result = eval(label.cget("text"))
        label.config(text=str(result))
    except Exception as e:
        label.config(text="ERROR")

window = Tk()
window.geometry("250x300")

label = Label(window, text="0", font=("Times New Roman", 20), pady=20)
label.place(x=0, y=0)

frame_button = Frame(window)
frame_button.place(x=0, y=70)

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        button = Button(frame_button, text=text, font=("Arial", 15), padx=18, pady=10, bg="Maroon", fg="White", command=clear)
    elif text == '=':
        button = Button(frame_button, text=text, font=("Arial", 15), padx=18, pady=10, command=calculate)
    else:
        button = Button(frame_button, text=text, font=("Arial", 15), padx=18, pady=10, command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

window.mainloop()
