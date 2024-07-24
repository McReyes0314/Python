"""
Features:
- Add tasks to the list
- Delete selected tasks
- Mark tasks as completed
- Save the list to a file
- Load the list from a file
"""

import tkinter as tk
from tkinter import messagebox, filedialog


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.task = []

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        self.add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        pass

    def delete_task(self):
        pass

    def mark_task(self):
        pass

    def save_task(self):
        pass

    def load_task(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()