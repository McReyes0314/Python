from tkinter import *
from tkinter import filedialog

window = Tk()


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\clair\\OneDrive\\Desktop",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    if file is None:
        return
    
    fileText = str(Text.get(1.0, END))
    file.write(fileText)
    file.close()


Text = Text(window, font=("Arial"))
Text.pack()
button = Button(text="Save", command=saveFile)
button.pack()


window.mainloop()