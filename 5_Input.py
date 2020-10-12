from tkinter import * #import everything

root = Tk()
root.title("Rath Progs")
root.geometry("500x500")


#Entry() function to get info from user and print it
Enttrii = Entry(root, width=50, fg="red", bg="yellow", borderwidth=10)
Enttrii.pack()
Enttrii.get()
Enttrii.insert(0, "Enter Your name...")

#place the '.get()' function in 'text=' so that it generates the text entered
def Clik():
    Hellow = "Hello " + Enttrii.get()
    Lab = Label(root, text=Hellow)
    Lab.pack()

#command=functionName will enable it
Butto = Button(root, text="Click me!", command=Clik, fg="yellow", bg="purple")

Butto.pack()


root.mainloop()