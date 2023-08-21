#learning Imaging with Tkinter
#working with radio buttons
#IntVar for integer and StringVar for string
from tkinter import *
root=Tk()
def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

    
modes=[
    ("pepperoni","pepperoni"),
    ("cheese","cheese"),
    ("Mushroom","Mushroom"),
    ("onion","onion"),
]
pizza=StringVar()
pizza.set("pepperoni")
for text,mode in modes:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)
#r = IntVar()
#r.set("2")

#Radiobutton(root, text="Option1", variable=r, value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option2", variable=r, value=2,command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option3", variable=r, value=3,command=lambda:clicked(r.get())).pack()

mylabel = Label(root, text=pizza.get())
mylabel.pack()

mybutton= Button(root,text="click me",command=lambda:clicked(pizza.get()))
mybutton.pack()
root.mainloop()

