from tkinter import *

root = Tk()
root.title("RathProg")
root.geometry("150x250")

def clic(): 
    Lab = Label(root, text="Heyya")
    Lab.pack()


frame = LabelFrame(root, text ="Button_Frame", padx=10, pady=10)
frame.pack(padx=10, pady=10)

butt = Button(frame, text ="button", command=clic, fg="yellow", bg="purple", padx=50)
butt.pack()


root.mainloop()