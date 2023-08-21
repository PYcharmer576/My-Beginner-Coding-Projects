# program to make new windows with tkinter
from tkinter import*
root=Tk()
root.title("New window")

def open():
 top=Toplevel()
 lbl=Label(top,text="Hello world").pack()
 bttn2=Button(top,text="close window",command=top.destroy).pack()
 

bttn=Button(root,text="open new window",command=open).pack()









mainloop()