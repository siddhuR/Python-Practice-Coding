from tkinter import*
root = Tk()
c=Canvas(root, bg="blue",height=700, width=1200, cursor='penoil')
id=c.create_line(50, 50, 200, 50, 200, 150, width=4, fill="white")
id=c.create_ovel(100, 100, 400, 300, width=5, fill="yellow", outline="red", activefill="green")
id=c.create_polygon(10, 10, 200, 200, 300, 200, width=5, fill="green", outline="red", smooth=1, activefill="lightblue")
id=c.create_rectangle(500, 200, 700, 600, width=2, fill="gray", outline="black", activefill="green")
c.pack()
root.mainloop()