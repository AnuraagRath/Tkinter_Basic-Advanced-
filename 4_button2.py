from tkinter import * #import everything

root = Tk()
root.title("Rath Progs")
root.geometry("500x500")

#create a function to print text when button is clicked
def Clik():
    Lab = Label(root, text="Heyya!!!")
    Lab.pack()

#command=functionName will enable it
Butto = Button(root, text="Click me!", command=Clik, fg="yellow", bg="purple")

Butto.pack()


root.mainloop()