#Write a Python GUI program to create a Checkbutton widget using tkinter module.

from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text ='Siddhu', font = "50")
w.pack()

Checkbutton1 = IntVar()

Button1 = Checkbutton(root, text = "Python", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 10)
	
Button1.pack()
mainloop()
