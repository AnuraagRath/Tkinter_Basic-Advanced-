from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("rathProg")

#notworking for ParrotOS
root.filename = filedialog.askopenfilename(initialdir="file:///home/user/Desktop", title="Select file", filetypes=(("png files", "*.png"),("all files", "*.*")))


root.mainloop()