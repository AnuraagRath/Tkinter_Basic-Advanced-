from tkinter import * #import everything

root = Tk()
root.title("Rath Progs")
root.geometry("500x500")


# Disabled State => Buttoi = Button(root, text="Click me!", state=DISABLED, fg="yellow", bg="purple")
# padx, pady changes size of button
Butto = Button(root, text="Click me!", padx=100, fg="yellow", bg="purple")

#Buttoi.pack()
Butto.pack()


root.mainloop()