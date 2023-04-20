#Write a Python GUI program to create two buttons exit and hello using tkinter module.

import tkinter as tk   
def write_text():
    print("hello...!")

a = tk.Tk()
frame = tk.Frame(a)
frame.pack()

text_disp= tk.Button(frame, text="Hello", command=write_text)
text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame, text="Exit", fg="green", command=quit)
exit_button.pack(side=tk.RIGHT)

a.mainloop()
