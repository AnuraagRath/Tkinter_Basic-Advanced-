from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("rathProg")


def popUp():
    resp = messagebox.showinfo("This is my popup", "Heyyyya")
    Label(root, text=resp).pack()

def popUp2():
    resp2 = messagebox.showwarning("This is my popup", "Heyyyya")
    Label(root, text=resp2).pack()

def popUp3():
    resp3 = messagebox.showerror("This is my popup", "Heyyyya")
    Label(root, text=resp3).pack()

def popUp4():
    resp4 = messagebox.askquestion("This is my popup", "Heyyyya")
    Label(root, text=resp4).pack()

def popUp5():
    resp5 = messagebox.askokcancel("This is my popup", "Heyyyya")
    Label(root, text=resp5).pack()

def popUp6():
    resp6 = messagebox.askyesno("This is my popup", "Heyyyya")
    Label(root, text=resp6).pack()


but1 = Button(root, text="Pop-Up", command=popUp)
but2 = Button(root, text="Pop-Up", command=popUp2)
but3 = Button(root, text="Pop-Up", command=popUp3)
but4 = Button(root, text="Pop-Up", command=popUp4)
but5 = Button(root, text="Pop-Up", command=popUp5)
but6 = Button(root, text="Pop-Up", command=popUp6)

but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()

root.mainloop()