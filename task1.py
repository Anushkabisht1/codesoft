from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Entry box
e = Entry(root, width=20, borderwidth=5, font=("Arial", 14))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global variables
f_num = None
math_op = ""

# Number button click
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Clear button
def button_clear():
    e.delete(0, END)

# Operation buttons
def button_operation(op):
    global f_num, math_op
    try:
        f_num = int(e.get())
        math_op = op
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Equal button
def button_equal():
    try:
        second_number = int(e.get())
        e.delete(0, END)
        if math_op == "add":
            e.insert(0, f_num + second_number)
        elif math_op == "sub":
            e.insert(0, f_num - second_number)
        elif math_op == "mul":
            e.insert(0, f_num * second_number)
        elif math_op == "div":
            if second_number == 0:
                e.insert(0, "Divide by 0 Error")
            else:
                e.insert(0, f_num / second_number)
    except:
        e.insert(0, "Error")


# Number Buttons
button_1 = Button(root, text="1", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,bg="#ADD8E6", command=lambda: button_click(0))

# Operation Buttons
button_add = Button(root, text="+", padx=40, pady=20,bg="light pink", command=lambda: button_operation("add"))
button_sub = Button(root, text="-", padx=42, pady=20,bg="light pink", command=lambda: button_operation("sub"))
button_mul = Button(root, text="*", padx=42, pady=20,bg="light pink", command=lambda: button_operation("mul"))
button_div = Button(root, text="/", padx=42, pady=20,bg="light pink" ,command=lambda: button_operation("div"))
button_equal = Button(root, text="=", padx=90, pady=20,bg="#ffdc6a", command=button_equal)
button_clear = Button(root, text="Clear", padx=80, pady=20,bg="#e49bfd", command=button_clear)

# Place buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=1)
button_mul.grid(row=6, column=2)

button_div.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()