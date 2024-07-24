from tkinter import *

window = Tk()

def openFile():
    print("File has been open")

def saveFile():
    print("File has been save")

def Cut():
    pass

def Copy():
    pass

def Paste():
    pass


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=Cut)
editMenu.add_command(label="Copy", command=Copy)
editMenu.add_command(label="Paste", command=Paste)
window.mainloop()