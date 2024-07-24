from tkinter import *
from tkinter import messagebox


def clear():
    bookTitle.delete(0, END)
    author.delete(0, END)
    price.delete(0, END)
    quantity.delete(0, END)


def add():
    title = bookTitle.get()
    auth = author.get()
    pri = price.get()
    quan = quantity.get()

    newBook = [title, auth, pri, quan]
    book.append(newBook)

    messagebox.showinfo("Book Added", "Book is added")


def inventory():
    inventoryWindow = Toplevel(window)
    inventoryWindow.title("Inventory")
    inventoryWindow.geometry("400x400")

    inventoryText = Text(inventoryWindow)
    inventoryText.pack(expand=True, fill=BOTH)

    inventoryText.insert(END, "Title\tAuthor\tPrice\tQuantity\n")
    inventoryText.insert(END, "-"*50 + "\n")

    for b in book:
        inventoryText.insert(END, f"{b[0]}\t{b[1]}\t{b[2]}\tb{3}\n")


window = Tk()

book = []

window.geometry("250x350")
window.resizable = False
label = Label(text="Book Selling System", font=("Times New Roman", 20), pady=20)
label.place(x=10, y=0)

frame = Frame(window)
frame.place(x=10, y=80)

bookTitleLabel = Label(frame, text="Book title:", font=("Arial", 10), pady=5)
bookTitleLabel.grid(row=0, column=0)

bookTitle = Entry(frame, width=25)
bookTitle.grid(row=0, column=1)

authorLabel = Label(frame, text="Author:", font=("Arial", 10), pady=5)
authorLabel.grid(row=1, column=0)
author = Entry(frame, width=25)
author.grid(row=1, column=1)

priceLabel = Label(frame, text="Price:", font=("Arial", 10), pady=5)
priceLabel.grid(row=2, column=0)
price = (Entry(frame, width=25))
price.grid(row=2, column=1)

quantityLabel = Label(frame, text="Price:", font=("Arial", 10), pady=5)
quantityLabel.grid(row=3, column=0)
quantity = Entry(frame, width=25)
quantity.grid(row=3, column=1)

addButton = Button(window, text="Add", font=("Arial", 10), width=15, bg="Maroon", fg="White", command=add)
addButton.place(x=100, y=220)

clearButton = Button(window, text="Clear", font=("Arial", 10), width=15, bg="Maroon", fg="White", command=clear)
clearButton.place(x=100, y=260)

inventoryButton = Button(window, text="Inventory", font=("Arial", 10), width=15, bg="Maroon", fg="White", command=inventory)
inventoryButton.place(x=100, y=300)

window.mainloop()