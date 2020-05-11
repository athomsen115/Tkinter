from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=8)
e.grid(row=0, column=0, columnspan=4)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def add():
    first_number = e.get()
    global f_num, math
    f_num = int(first_number)
    math = "add"
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global f_num, math
    f_num = int(first_number)
    math = "subtract"
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num, math
    f_num = int(first_number)
    math = "multiply"
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num, math
    f_num = int(first_number)
    math = "divide"
    e.delete(0, END)

def clear():
    e.delete(0, END)

def equals():
    second_number = e.get()
    e.delete(0, END)
    global f_num, math
    math = math.upper()[0]
    
    if math == "A":
        e.insert(0, f_num + int(second_number))
    elif math == "S":
        e.insert(0, f_num - int(second_number))
    elif math == "M":
        e.insert(0, f_num * int(second_number))
    elif math == "D":
        e.insert(0, f_num / int(second_number))
        

# Button Definitions
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
button_period = Button(root, text=".", padx=40, pady=20, command=lambda : button_click("."))
button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
button_divide = Button(root, text="/", padx=39, pady=20, command=divide)
button_multiply = Button(root, text="*", padx=39, pady=20, command=multiply)
button_equal = Button(root, text="=", padx=91, pady=20, command=equals)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear)
    
#Put Buttons on the Screen
button_1.grid(row= 4, column= 0)
button_2.grid(row= 4, column= 1)
button_3.grid(row= 4, column= 2)

button_4.grid(row= 3, column= 0)
button_5.grid(row= 3, column= 1)
button_6.grid(row= 3, column= 2)

button_7.grid(row= 2, column= 0)
button_8.grid(row= 2, column= 1)
button_9.grid(row= 2, column= 2)

button_0.grid(row= 5, column= 1)
button_period.grid(row = 5, column = 0)

button_add.grid(row= 4, column= 3)
button_subtract.grid(row= 3, column= 3)
button_multiply.grid(row= 2, column= 3)
button_divide.grid(row= 1, column= 3)

button_clear.grid(row= 1, column= 0, columnspan=2)
button_equal.grid(row= 5, column= 2, columnspan=2)

root.mainloop()