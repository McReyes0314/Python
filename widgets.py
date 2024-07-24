from tkinter import *
from tkinter import  ttk

def buttonClick():
    enteredText = entry.get()
    label.config(text=f"{enteredText}")

def listboxSelect(event):
    selected_item = listbox.get(listbox.curselection())
    label.config(text=f"selected: {selected_item}")

def dropdownSelect(option):
    label.config(text=f"Selected: {option}")

# Create the main window
window = Tk()
window.title("Advance Tkinter App")
# Create a label widget
label = Label(window, text="Text", font=("Helvetica", 14))
label.pack(pady=0)

# Create an Entry widget
entry = Entry(window, width=40)
entry.pack(pady=10)

# Create a listbox widget
listbox = Listbox(window)
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in items:
    listbox.insert(END, item)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", listboxSelect)

# Create a Button widget
button = Button(window, text="Display Text", command=buttonClick)
button.pack(pady=10)

# Create a Dropdown menu
dropdown_var = StringVar(value="Choose an option")
dropdown = ttk.Combobox(window, textvariable=dropdown_var)
dropdown['values'] = ["Option 1", "Option 2", "Option 3"]
dropdown.pack(pady=10)
dropdown.bind("<<ComboboxSelection>>", lambda event: dropdownSelect(dropdown_var.get()))

window.mainloop()
