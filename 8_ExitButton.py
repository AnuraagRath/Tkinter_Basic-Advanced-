from tkinter import * #import everything

root = Tk()
root.title("ExitButton")
root.geometry("100x100")

but = Button(root, text="Exit", padx=50, command=exit, fg="yellow", bg="purple")
but.pack()

root.mainloop()