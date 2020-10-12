from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title("ExitButton")

myImg = ImageTk.PhotoImage(Image.open("rathVille.png")) 
la_Bel = Label(root, image=myImg)
la_Bel.pack()

root.mainloop()