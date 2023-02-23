from tkinter import *

NAME = "Tkinter"

root = Tk()
root.geometry('250x180')
root.resizable(False, False)
root.title(NAME)

m = Menu(root)

fm = Menu(m)
fm.add_command(label="Close", command=root.destroy)
    
m.add_cascade(label="File", menu=fm)

Label(root, text="Hello, world!", font=("Lucida Console", 17)).place(x=30, y=80)

root.config(menu=m)

root.mainloop()
