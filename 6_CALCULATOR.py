from tkinter import * #import everything

root = Tk()
root.title("Rath_CalC")


Enttrii = Entry(root, width=35, fg="red", bg="yellow", borderwidth=10)
Enttrii.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
Enttrii.get()


#define buttons
#Current -> gets the current value entered, 
#  '.delete' deletes additional values and '.insert' will insert the two 
def ButtonClick(num):
    Current = Enttrii.get()
    Enttrii.delete(0, END)
    Enttrii.insert(0, str(Current) + str(num))

def ButCl():
    Enttrii.delete(0, END) 

#create GlobalVariable so that it can be called elsewhere
#GlobalVar should be an Integer, Delete values after entry '.delete' 
def ButAd():
    firstNum = Enttrii.get()
    global f_Num 
    global math
    math = "Add"
    f_Num = int(firstNum)
    Enttrii.delete(0, END)

def ButSub():
    firstNum = Enttrii.get()
    global f_Num 
    global math
    math = "Sub"
    f_Num = int(firstNum)
    Enttrii.delete(0, END)

def ButMul():
    firstNum = Enttrii.get()
    global f_Num 
    global math
    math = "Mul"
    f_Num = int(firstNum)
    Enttrii.delete(0, END)  

def Butdiv():
    firstNum = Enttrii.get()
    global f_Num 
    global math
    math = "Div"
    f_Num = int(firstNum)
    Enttrii.delete(0, END)


def ButEq():
    secondNumber = Enttrii.get()
    Enttrii.delete(0, END)
    
    if math == "Add":
        Enttrii.insert(0, f_Num + int(secondNumber))
    elif math == "Sub":
        Enttrii.insert(0, f_Num - int(secondNumber))
    elif math == "Mul":
        Enttrii.insert(0, f_Num * int(secondNumber))
    else:
        Enttrii.insert(0, f_Num / int(secondNumber))            




Button1 = Button(root, text="1", padx = 40, pady=20, command=lambda: ButtonClick(1), fg="yellow", bg="purple")
Button2 = Button(root, text="2", padx = 40, pady=20, command=lambda: ButtonClick(2), fg="yellow", bg="purple")
Button3 = Button(root, text="3", padx = 40, pady=20, command=lambda: ButtonClick(3), fg="yellow", bg="purple")
Button4 = Button(root, text="4", padx = 40, pady=20, command=lambda: ButtonClick(4), fg="yellow", bg="purple")
Button5 = Button(root, text="5", padx = 40, pady=20, command=lambda: ButtonClick(5), fg="yellow", bg="purple")
Button6 = Button(root, text="6", padx = 40, pady=20, command=lambda: ButtonClick(6), fg="yellow", bg="purple")
Button7 = Button(root, text="7", padx = 40, pady=20, command=lambda: ButtonClick(7), fg="yellow", bg="purple")
Button8 = Button(root, text="8", padx = 40, pady=20, command=lambda: ButtonClick(8), fg="yellow", bg="purple")
Button9 = Button(root, text="9", padx = 40, pady=20, command=lambda: ButtonClick(9), fg="yellow", bg="purple")
Button0 = Button(root, text="0", padx = 40, pady=20, command=lambda: ButtonClick(0), fg="yellow", bg="purple")

ButtonAdd = Button(root, text="+", padx = 39, pady= 20, command=ButAd, fg="yellow", bg="green")
ButtonSub = Button(root, text="_", padx = 41, pady= 20, command=ButSub, fg="yellow", bg="green")
ButtonMul = Button(root, text="*", padx = 40, pady= 20, command=ButMul, fg="yellow", bg="green")
ButtonDiv = Button(root, text="/", padx = 40, pady= 20, command=Butdiv, fg="yellow", bg="green")

ButtonEqual = Button(root, text="=", padx = 91, pady= 20, command=ButEq, fg="yellow", bg="blue")
ButtonClear = Button(root, text="Clear", padx = 79, pady= 20, command=ButCl, fg="yellow", bg="blue")

#put buttons on screen
Button1.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button3.grid(row=3,column=2)

Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)

Button7.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button9.grid(row=1,column=2)

Button0.grid(row=4,column=0)

ButtonAdd.grid(row=5,column=0)
ButtonSub.grid(row=6,column=0)
ButtonMul.grid(row=6,column=1)
ButtonDiv.grid(row=6,column=2)

ButtonEqual.grid(row=5,column=1,columnspan=2)
ButtonClear.grid(row=4,column=1, columnspan=2)


root.mainloop()