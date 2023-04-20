#Write a Python GUI program to create a label and change the label font style (font name, bold, size) using tkinter module.

import tkinter as tk
a = tk.Tk()
a.title("label font style using tkinter module")
my_label = tk.Label(a, text="Hello", font=("MV boli", 80))
my_label.grid(column=0, row=0)
a.mainloop()