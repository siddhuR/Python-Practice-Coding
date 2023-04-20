#Write a Python GUI program to create a Spinbox widget using tkinter module.

from tkinter import *
root = Tk()
root.geometry("300x200")

w = Label(root, text ='Siddhartha', font = "50")
w.pack()
sp = Spinbox(root, from_= 0, to = 20)
sp.pack()
root.mainloop()
