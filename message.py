from tkinter import *
root= Tk()
nextframe1=Frame(root, bg="red", highlightbackground="green", highlightthickness=5)
nextframe1.grid(row=1,column=0)

m=Message(nextframe1, text='This is message that has more than one line of text.', width=200, font=('Times New Roman', -10,'bold italic'))
m.pack(side=LEFT)
root.mainloop()