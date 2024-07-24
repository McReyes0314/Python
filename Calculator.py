from tkinter import *

window = Tk()
window.geometry("250x300")
label = Label(text=0, font=("Times New Roman", 20), pady=20)
label.place(x=0, y=0)

frame_button = Frame(window)
frame_button.place(x=0, y=70)

button7 = Button(frame_button, text=7, font=("Arial", 15), padx=18, pady=10).grid(row=0, column=0)
button8 = Button(frame_button, text=8, font=("Arial", 15), padx=18, pady=10).grid(row=0, column=1)
button9 = Button(frame_button, text=9, font=("Arial", 15), padx=18, pady=10).grid(row=0, column=2)
buttonPlus = Button(frame_button, text="+", font=("Arial", 15), padx=18, pady=10).grid(row=0, column=3)

button4 = Button(frame_button, text=4, font=("Arial", 15), padx=18, pady=10).grid(row=1, column=0)
button5 = Button(frame_button, text=5, font=("Arial", 15), padx=18, pady=10).grid(row=1, column=1)
button6 = Button(frame_button, text=6, font=("Arial", 15), padx=18, pady=10).grid(row=1, column=2)
buttonMinus = Button(frame_button, text="-", font=("Arial", 15), padx=21, pady=10).grid(row=1, column=3)

button1 = Button(frame_button, text=1, font=("Arial", 15), padx=18, pady=10).grid(row=2, column=0)
button2 = Button(frame_button, text=2, font=("Arial", 15), padx=18, pady=10).grid(row=2, column=1)
button3 = Button(frame_button, text=3, font=("Arial", 15), padx=18, pady=10).grid(row=2, column=2)
buttonMulti = Button(frame_button, text="*", font=("Arial", 15), padx=20, pady=10).grid(row=2, column=3)

buttonC = Button(frame_button, text="c", font=("Arial", 15), padx=18, pady=10, bg="Maroon", fg="White").grid(row=3, column=0)
button0 = Button(frame_button, text=0, font=("Arial", 15), padx=18, pady=10).grid(row=3, column=1)
buttonEqual = Button(frame_button, text="=", font=("Arial", 15), padx=18, pady=10).grid(row=3, column=2)
buttonDiv = Button(frame_button, text="/", font=("Arial", 15), padx=20, pady=10).grid(row=3, column=3)

window.mainloop()