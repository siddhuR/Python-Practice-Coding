#Write a Python GUI program to create a window and disable to resize the window using tkinter module.

import tkinter as tk
a = tk.Tk()
a.title("-Hello-")
a.resizable(0,0)
a.mainloop()
