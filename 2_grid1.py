from tkinter import *

root = Tk()
root.title("Rath Progs")
root.geometry("500x500")

Label1 = Label(root, text ="Heyyyy", fg="yellow", bg="red")
Label2 = Label(root, text ="Hey")

Label1.grid(row=0, column=0)
Label2.grid(row=1, column=1)

root.mainloop()