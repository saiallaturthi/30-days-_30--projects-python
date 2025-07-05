from tkinter import *

mw = Tk()
mw.title("Calculator")

# Clear display
def clear():
    db.delete(0, END)

# Append number to display
def btn_clk(num):
    cur_num = db.get()
    clear()
    f_num = cur_num + num
    db.insert(0, f_num)

first_num = 0
operator = ""

# Set the operator and store first number
def set_operator(op):
    global first_num, operator
    first_num = float(db.get())
    operator = op
    db.delete(0, END)
    db.insert(0, op)  # Optional: Show operator temporarily

# Perform calculation
def calculate():
    try:
        second_text = db.get()
        # Handle if display still shows the operator
        if second_text == operator:
            return
        second_num = float(second_text)
        result = 0
        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result = first_num * second_num
        elif operator == "/":
            if second_num == 0:
                db.delete(0, END)
                db.insert(0, "Error")
                return
            result = first_num / second_num
        db.delete(0, END)
        db.insert(0, str(result))
    except:
        db.delete(0, END)
        db.insert(0, "Error")

# Entry display
db = Entry(mw, width=14, font=("Arial", 28), justify=RIGHT)

# Buttons 0–9
btns = [Button(mw, text=str(i), padx=36, pady=10, font=("Arial", 14),
               command=lambda i=i: btn_clk(str(i))) for i in range(10)]

# Operator & control buttons
btn_clear = Button(mw, text="Clear", padx=72, pady=10, font=("Arial", 14), command=clear)
btn_div = Button(mw, text="/", padx=36, pady=10, font=("Arial", 14), command=lambda: set_operator("/"))
btn_mul = Button(mw, text="*", padx=36, pady=10, font=("Arial", 14), command=lambda: set_operator("*"))
btn_equal = Button(mw, text="=", padx=36, pady=45, font=("Arial", 14), command=calculate)
btn_add = Button(mw, text="+", padx=36, pady=10, font=("Arial", 14), command=lambda: set_operator("+"))
btn_sub = Button(mw, text="-", padx=36, pady=10, font=("Arial", 14), command=lambda: set_operator("-"))

# Grid layout
db.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
btns[1].grid(row=3, column=0, padx=2, pady=2)
btns[2].grid(row=3, column=1, padx=2, pady=2)
btns[3].grid(row=3, column=2, padx=2, pady=2)
btns[4].grid(row=2, column=0, padx=2, pady=2)
btns[5].grid(row=2, column=1, padx=2, pady=2)
btns[6].grid(row=2, column=2, padx=2, pady=2)
btns[7].grid(row=1, column=0, padx=2, pady=2)
btns[8].grid(row=1, column=1, padx=2, pady=2)
btns[9].grid(row=1, column=2, padx=2, pady=2)
btns[0].grid(row=4, column=0, padx=2, pady=2)

btn_clear.grid(row=4, column=1, padx=2, pady=2, columnspan=2)
btn_div.grid(row=5, column=0, padx=2, pady=2)
btn_mul.grid(row=5, column=1, padx=2, pady=2)
btn_equal.grid(row=5, column=2, padx=2, pady=2, rowspan=2)
btn_add.grid(row=6, column=0, padx=2, pady=2)
btn_sub.grid(row=6, column=1, padx=2, pady=2)

mw.mainloop()
