from tkinter import *
def sel():
    x=var1.get()
    print("you selected"+str(x))
root= Tk()

root.geometry("300x300")
frame1=Frame(root, bg="red", highlightbackground="green", highlightthickness=5)
frame1.grid(row=0,column=0)
menubar = Menu(root)
root.config(menu=menubar)
filemenu= Menu(frame1, tearoff=0)
frame=Frame(root, bg="red", highlightbackground="green", highlightthickness=5)
frame.grid(row=1,column=0)

label1=Label(frame, text="wellcome to Python", width=20, height=2, font="Courier -10 bold underline", fg='blue', bg='yellow')
redbutton=Button(frame, text="Red", fg="red", bg="white")
redbutton.pack(side=LEFT)

val1=IntVar()
spin1=Spinbox(frame, from_=5, to=15, textvariable=val1, width=15, fg='blue', bg='yellow', font=('Arial',14,'bold') )
spin1.pack(side=LEFT)
val2=StringVar()
spin2=Spinbox(frame, values=('Hyderabad','Delhi','Culcuta','Mumbai'), 
              textvariable=val2, width=15, fg='black', bg='yellow', font=('Arial',14,'bold') )
spin2.pack(side=LEFT)

a=val1.get()
b=val2.get()
label2=Label(frame, text=b, width=20, height=2, font="Courier -10 bold underline", fg='blue', bg='yellow')
label2.pack(side=LEFT)
lb=Listbox(frame, font= "Arial 12 bold", fg='blue', bg='yellow', height=8, width=24, activestyle='underline', 
           selectmode=SINGLE)
lb.insert(1, "Python")
lb.insert(2, "Perl")
lb.insert(3, "C")
lb.insert(4, "PHP")
lb.insert(5, "JSP")
lb.insert(6, "Ruby")
lb.pack(side=LEFT)

var1=IntVar()
Radio1=Radiobutton(frame, text="Option1", variable=var1, value=1, command=sel)
Radio1.pack()
Radio2=Radiobutton(frame, text="Option2", variable=var1, value=2, command=sel)
Radio2.pack()
Radio3=Radiobutton(frame, text="Option3", variable=var1, value=3, command=sel)
Radio3.pack()
root.mainloop()