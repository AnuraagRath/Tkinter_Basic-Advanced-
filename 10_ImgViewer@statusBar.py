from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewer")

myImg1 = ImageTk.PhotoImage(Image.open("rathVille.png")) 
myImg2 = ImageTk.PhotoImage(Image.open("rathVille6.png")) 
myImg3 = ImageTk.PhotoImage(Image.open("rathVille3.png"))
myImg4 = ImageTk.PhotoImage(Image.open("rathVille4.png")) 
myImg5 = ImageTk.PhotoImage(Image.open("rathVille5.png")) 

image_list = [myImg1, myImg2, myImg3, myImg4, myImg5]

#status bar to show which image we r lookin at
status = Label(root, text="Img 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #anchor towards the right so E=East
status.grid(row =2, column=0, columnspan = 3, sticky=W+E) 
#Sticky makes ur label to stretch, so stretch across the window from West to east therefore 'W+E'
#refer Def Forward and Backward

la_Bel = Label(root, image=myImg1)
la_Bel.grid(row = 0, column = 0, columnspan = 3)

def Forward(imgMove):
    global la_Bel
    global butFor
    global butBack 

    la_Bel.grid_forget()
    la_Bel = Label(image = image_list[imgMove-1])
    butFor = Button(root, text=">>", command= lambda: Forward(imgMove+1), fg="yellow", bg="purple")
    butBack = Button(root, text="<<", command=lambda: Backward(imgMove-1), fg="yellow", bg="purple")
    
    if imgMove == 5:
        butFor = Button(root, text=">>", state=DISABLED) 


    la_Bel.grid(row = 0, column = 0, columnspan = 3)
    
    butBack.grid(row = 1,  column = 0)  
    butFor.grid(row = 1, column = 2 )

    #add imgMove so that everypage wil update as to which image it is
    status = Label(root, text="Img " + str(imgMove) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #anchor towards the right so E=East
    status.grid(row =2, column=0, columnspan = 3, sticky=W+E) 


def Backward(imgMove):
    global la_Bel
    global butFor
    global butBack


    la_Bel.grid_forget()
    la_Bel = Label(image = image_list[imgMove-1])
    butFor = Button(root, text=">>", command=lambda: Forward(imgMove+1), fg="yellow", bg="purple")
    butBack = Button(root, text="<<", command=lambda: Backward(imgMove-1), fg="yellow", bg="purple")
    
    if imgMove == 1:
        butBack = Button(root, text="<<", state=DISABLED) 

    la_Bel.grid(row = 0, column = 0, columnspan = 3)
    
    butBack.grid(row = 1,  column = 0)  
    butFor.grid(row = 1, column = 2 )
    
    #add imgMove so that everypage wil update as to which image it is
    status = Label(root, text="Img " + str(imgMove) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #anchor towards the right so E=East
    status.grid(row =2, column=0, columnspan = 3, sticky=W+E) 



butBack = Button(root, text="<<", command=Backward, state=DISABLED, fg="yellow", bg="purple")
butFor = Button(root, text=">>", command=lambda: Forward(2), fg="yellow", bg="purple")
butExit = Button(root, text="EXIT", command=exit, fg="yellow", bg="red", padx = 50)

butBack.grid(row = 1,  column = 0)
butFor.grid(row = 1, column = 2 )
butExit.grid(row = 1, column = 1)


root.mainloop()