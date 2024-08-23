# Python-based calculator that can perform basic arithmetic operations through a
# command-line interface or a simple GUI.

import tkinter as tk

field_text = ""

def add_to_field(sth):
    global field_text
    field_text += str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

def calculate():
    global field_text
    try:
        result = str(eval(field_text))
        field.delete("1.0", "end")
        field.insert("1.0", result)
    except:
        field.delete("1.0", "end")
        field.insert("1.0", "Error")

def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")

# Example usage
Window = tk.Tk()
Window.geometry("300x300")

field = tk.Text(Window, height=2, width=21, font=("Times New Roman", 20))
field.grid(row=1, column=1, columnspan=4)

##################################
# Number Buttons
##################################

btn_1 = tk.Button(Window, text="1", command=lambda: add_to_field(1), width=5, font=("Times New Roman", 14))
btn_1.grid(row=4, column=1)

btn_2 = tk.Button(Window, text="2", command=lambda: add_to_field(2), width=5, font=("Times New Roman", 14))
btn_2.grid(row=4, column=2)

btn_3 = tk.Button(Window, text="3", command=lambda: add_to_field(3), width=5, font=("Times New Roman", 14))
btn_3.grid(row=4, column=3)

btn_4 = tk.Button(Window, text="4", command=lambda: add_to_field(4), width=5, font=("Times New Roman", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(Window, text="5", command=lambda: add_to_field(5), width=5, font=("Times New Roman", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(Window, text="6", command=lambda: add_to_field(6), width=5, font=("Times New Roman", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(Window, text="7", command=lambda: add_to_field(7), width=5, font=("Times New Roman", 14))
btn_7.grid(row=2, column=1)

btn_8 = tk.Button(Window, text="8", command=lambda: add_to_field(8), width=5, font=("Times New Roman", 14))
btn_8.grid(row=2, column=2)

btn_9 = tk.Button(Window, text="9", command=lambda: add_to_field(9), width=5, font=("Times New Roman", 14))
btn_9.grid(row=2, column=3)

btn_0 = tk.Button(Window, text="0", command=lambda: add_to_field(0), width=5, font=("Times New Roman", 14))
btn_0.grid(row=5, column=1)

##################################
# Operation Buttons
##################################

btn_plus = tk.Button(Window, text="+", command=lambda: add_to_field("+"), width=5, font=("Times New Roman", 14))
btn_plus.grid(row=4, column=4)

btn_minus = tk.Button(Window, text="-", command=lambda: add_to_field("-"), width=5, font=("Times New Roman", 14))
btn_minus.grid(row=5, column=4)

btn_times = tk.Button(Window, text="*", command=lambda: add_to_field("*"), width=5, font=("Times New Roman", 14))
btn_times.grid(row=3, column=4)

btn_division = tk.Button(Window, text="/", command=lambda: add_to_field("/"), width=5, font=("Times New Roman", 14))
btn_division.grid(row=2, column=4)

btn_clear = tk.Button(Window, text="Clear", command=lambda: clear(), width=5, font=("Times New Roman", 14))
btn_clear.grid(row=5, column=3)

btn_decimal = tk.Button(Window, text=".", command=lambda: add_to_field("."), width=5, font=("Times New Roman", 14))
btn_decimal.grid(row=5, column=2)

btn_open_parenthesis = tk.Button(Window, text="(", command=lambda: add_to_field("("), width=5, font=("Times New Roman", 14))
btn_open_parenthesis.grid(row=6, column=1)

btn_close_parenthesis = tk.Button(Window, text=")", command=lambda: add_to_field(")"), width=5, font=("Times New Roman", 14))
btn_close_parenthesis.grid(row=6, column=2)

btn_equal = tk.Button(Window, text="=", command=lambda: calculate(), width=12, font=("Times New Roman", 14))
btn_equal.grid(row=6, column=3, columnspan=2)

Window.mainloop()
