from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("rathProg")
root.geometry("500x200")


def popUp():
    resp = messagebox.askyesno("This is my popup", "Heyyyya")
    
    if resp == 1:
        Label(root, text="you selected YESSSSSS").pack()
    else:
        Label(root, text="you selected NOOOOOOO").pack()    

Button(root, text="Pop-Up", command=popUp).pack()

root.mainloop()