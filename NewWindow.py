from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("250x300")


label_txt_user = StringVar()
label_txt_pass = StringVar()

def login():
    default_username = "User123"
    default_password = "Pass****"
    user = username.get()
    passw = password.get()

    if user == default_username and passw == default_password:
        window.destroy()
        new_window = Tk()
        new_window.geometry("200x200")
        text = Label(new_window, text="Welcome", font=("Arial", 20))
        text.pack()
        new_window.mainloop()

    if user != default_username:
        label_txt_user.set("Invalid Username")

    if user == "":
        label_txt_user.set("Username is not filled")

    if passw != default_password:
        label_txt_pass.set("Invalid Password")

    if passw == "":
        label_txt_pass.set("Password is not filled")


user_error = Label(textvariable=label_txt_user, font=("Arial", 7), fg="Maroon")
user_error.place(x=10, y=130)

pass_error = Label(textvariable=label_txt_pass, font=("Arial", 7), fg="Maroon")
pass_error.place(x=10, y=210)

label = Label(text="Login", font=("Arial", 20), fg="Green", pady=10)
label.pack(side=TOP)

label1 = Label(text="Username", font=("Arial", 10))
label1.place(x=10, y=70)

username = Entry(font=("Arial", 15))
username.place(x=12, y=100)

label2 = Label(text="Password", font=("Arial", 10), pady=10)
label2.place(x=10, y=150)

password = Entry(font=("Arial", 15), show="*")
password.place(x=12, y=180)

login_button = Button(text="Login", font=("Arial", 13), bg="Green", fg="White", command=login)
login_button.place(x=185, y=240)

window.mainloop()
