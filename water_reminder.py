import tkinter as tk
from tkinter import messagebox

INTERVAL_MS = 60 * 60 * 1000  # 1 hour


def remind():
    messagebox.showinfo("Water reminder", "Time to drink some water!")
    root.after(INTERVAL_MS, remind)


root = tk.Tk()
root.withdraw()  # Keep the main window hidden
root.after(INTERVAL_MS, remind)
root.mainloop()
