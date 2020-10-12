from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("rathProg")
root.geometry("500x500")


def open():
    global myImg
    #Toplevel() creates a new window, so use top instead of root.
    top = Toplevel()
    myImg = ImageTk.PhotoImage(Image.open("rathVille.png"))
    lab = Label(top, image=myImg)
    lab.pack()
    btn2 = Button(top, text="Close", command=top.quit, fg="yellow", bg="red")
    btn2.pack()


butt = Button(root, text="OpenSesseme", command=open, fg="yellow", bg="purple") 
butt.pack()

root.mainloop()