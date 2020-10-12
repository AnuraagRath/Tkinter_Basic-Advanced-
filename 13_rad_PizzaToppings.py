from tkinter import *

root = Tk()
root.title("PizzaToppings")
root.geometry("500x500")

#create Tuples; 'text,topping(variable)' for Pizza toppings 
Toppings = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
    ("Corn", "Corn"),
    ("Chicken", "Chicken"),
    ("Sausage","Sausage"),
    ("Chicken Tikka","Chicken Tikka")
]

pizza = StringVar()
#pizza.set("Pepperoni")

#Loop the toppings
for text, topping in Toppings:
    Radiobutton(root, text=text, variable=topping, value=mode).pack(anchor=W)

def clicked(value):
    myLab = Label(root, text=value)
    myLab.pack()


myLab = Label(root, text=pizza.get())
myLab.pack()

myButton = Button(root, text="Clickme", fg="yellow", bg="purple", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()