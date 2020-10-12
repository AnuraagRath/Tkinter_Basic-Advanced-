from tkinter import *

root = Tk()
root.title("rathProg")
root.geometry("100x100")

r = IntVar()
r.set("2")


def clicked(value):
    myLab = Label(root, text=value)
    myLab.pack()

Radiobutton(root, text="option1", variable=r, value = 1).pack() 
#command=lambda: clicked(r.get()) can be used if u want to generate result even if u press the radiobutton
Radiobutton(root, text="option1", variable=r, value = 2).pack() 

myLab = Label(root, text=r.get())
myLab.pack()

myButton = Button(root, text="Clickme", command=lambda: clicked(r.get()))
myButton.pack()
root.mainloop()