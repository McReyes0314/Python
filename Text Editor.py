"""
Features:
- A text area for writing.
- A menu with options to open a file, save a file, and exit the application
"""

from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("400x400")


def openFile():
    file = filedialog.askopenfilename(initialdir="C:\\Users\\clair\\OneDrive\\Desktop",
                                      title="Open File",
                                      filetypes=[
                                          ("Text File", '.txt'),
                                          ("All Files", '.*')
                                      ])
    fileOpen = open(file, 'r')
    print(fileOpen.read())
    fileOpen.close()


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\clair\\OneDrive\\Desktop",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return

    fileText = str(text.get(1.0, END))
    file.write(fileText)
    file.close()


# text area to write
text = Text(window)
text.pack()

# menu with open, save, and exit
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

window.mainloop()
