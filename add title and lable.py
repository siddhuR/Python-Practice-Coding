#Write a Python GUI program to import Tkinter package and create a window. Set its title and add a label to the window.

import tkinter as tk
a = tk.Tk()
a.title("Adding title and inserting a label to the window")
var_label = tk.Label(a, text="Labeling")
var_label.grid(column=0, row=0)
a.mainloop()