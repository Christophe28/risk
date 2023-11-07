from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import os
import shutil
from pathlib import Path

executable_path = Path("./dist/index")
desktop = Path.home()

## Show message
def show_message():
  messagebox.showinfo("Message", "Les grosses couilles")

# Create window
window = Tk()
window.title("Multi risk")
window.iconbitmap("")
window.config(bg = "#87CEEB")

# Full screen size
width = window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

# Create button
button = Button(window, text = "Test", command=show_message)
button.pack(side = TOP, pady = 5)

window.mainloop()

