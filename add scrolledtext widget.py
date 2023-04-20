#Write a Python GUI program to create a Scrolled Text widgets using tkinter module.

import tkinter as tk
import tkinter.scrolledtext as ttk
a = tk.Tk()
a.title("Scrolledtext Widget")
a.geometry('350x200')
txt = ttk.ScrolledText(a, width=40, height=10)
txt.grid(column=0, row=0)
a.mainloop()