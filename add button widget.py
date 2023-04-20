#Write a Python GUI program to add a button in your application using tkinter module.

import tkinter as tk 
a = tk.Tk() 
a.title('Title - button') 
b_button = tk.Button(a, text='click here', height=1, width=35, command=a.destroy) 
b_button.pack() 
a.mainloop()
