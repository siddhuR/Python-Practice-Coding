#Write a Python GUI program to create a Listbox bar widgets using tkinter module.

import tkinter as tk
a = tk.Tk()
a.geometry("250x200")
label1 = tk.Label(a,text = "choose the city :")
listbox = tk.Listbox(a)
listbox.insert(1,"Hyderabad")
listbox.insert(2, "Chennai")
listbox.insert(3, "Mumbai")
listbox.insert(4, "Bangalore")
label1.pack()
listbox.pack()
a.mainloop()