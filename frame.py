from tkinter import*
root= Tk()
root.geometry("300x300")
frame=Frame(root,bg="red", highlightbackground="green", highlightthickness=5)
frame.grid(row=0,column=0)
label1=Label(frame, text="wellcome to python",width=20, height=3, font="courier -10 bold underline",fg='blue',bg='yellow')
label1.pack(side=BOTTOM)
root.mainloop()