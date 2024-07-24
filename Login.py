from tkinter import *

window = Tk()

default_username = "username"
default_password = "password123"


# button functions 
def login():
    global default_username
    global default_password

    usrnam = username.get()
    passw = password.get()

    if default_username == usrnam and default_password == passw:
        print("Welcome")
    else:
        print("Invalid Credentials")


window.geometry("300x300")
# label
username_label = Label(window,
                       text="Username",
                       font=("Arial", 10))
username_label.place(x=10, y=0)
password_label = Label(window,
                       text="Password",
                       font=("Arial", 10)
                       )
password_label.place(x=10, y=50)

# textfield
username = Entry(window,
                 font=("Arial", 15)
                 )
username.place(x=10, y=20)

password = Entry(window,
                 font=("Arial", 15),
                 show="*"
                 )
password.place(x=10, y=70)

# Button
login_button = Button(window, text="Login", command=login)
login_button.place(x=10, y=110)

window.mainloop()
