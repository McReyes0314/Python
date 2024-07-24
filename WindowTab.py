from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # widgets that manages a collection of windows

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")
# expand: fill any space not otherwise
# fill = fill space on x and y-axis

Label(tab1, text="Tab 1", width=50, height=25).pack()
Label(tab2, text="Tab 2", width=50, height=25).pack()

window.mainloop()