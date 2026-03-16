#! /usr/bin/python3
import tkinter.ttk as tk
import tkinter
import calc

w = tkinter.Tk()
w.title("Calculator")
w.geometry('132x165')


def plus(e):
    calc.set_math_sign(0)
    if calc.num_num == 0:
        example.config(text=str(calc.get_num()) + calc.get_sign())
    else:
        example.config(text=example.cget("text") + str(calc.get_num()))


def minus(e):
    calc.set_math_sign(1)
    if calc.num_num == 0:
        example.config(text=str(calc.get_num()) + calc.get_sign())
    else:
        example.config(text=example.cget("text") + str(calc.get_num()))


def multiply(e):
    calc.set_math_sign(2)
    if calc.num_num == 0:
        example.config(text=str(calc.get_num()) + calc.get_sign())
    else:
        example.config(text=example.cget("text") + str(calc.get_num()))


def divide(e):
    calc.set_math_sign(3)
    if calc.num_num == 0:
        example.config(text=str(calc.get_num()) + calc.get_sign())
    else:
        example.config(text=example.cget("text") + str(calc.get_num()))


def show_result(e):
    result.config(text=calc.calculate())


def add_to_num(e):
    calc.add_to_num(e.widget.cget("text"))
    result.config(text=calc.get_num())


def clear(e):
    calc.c()
    result.config(text="0")


go_res = tk.Button(w, text="=", width=2)
go_res.place(y=133, x=70)
go_res.bind("<Button-1>", show_result)

go_button = tk.Button(w, text="+", width=2)
go_button.place(y=43, x=100)
go_button.bind("<Button-1>", plus)

go_min = tk.Button(w, text="-", width=2)
go_min.place(y=73, x=100)
go_min.bind("<Button-1>", minus)

go_mul = tk.Button(w, text="*", width=2)
go_mul.place(y=103, x=100)
go_mul.bind("<Button-1>", multiply)

go_div = tk.Button(w, text="/", width=2)
go_div.place(y=133, x=100)
go_div.bind("<Button-1>", divide)

b1 = tk.Button(w, text='1', width=2)
b1.place(y=43, x=10)

b2 = tk.Button(w, text='2', width=2)
b2.place(y=43, x=40)

b3 = tk.Button(w, text='3', width=2)
b3.place(y=43, x=70)

b4 = tk.Button(w, text='4', width=2)
b4.place(y=73, x=10)

b5 = tk.Button(w, text='5', width=2)
b5.place(y=73, x=40)

b6 = tk.Button(w, text='6', width=2)
b6.place(y=73, x=70)

b7 = tk.Button(w, text='7', width=2)
b7.place(y=103, x=10)

b8 = tk.Button(w, text='8', width=2)
b8.place(y=103, x=40)

b9 = tk.Button(w, text='9', width=2)
b9.place(y=103, x=70)

b0 = tk.Button(w, text='0', width=2)
b0.place(y=133, x=40)

c = tk.Button(w, text='C', width=2)
c.place(y=133, x=10)

b0.bind("<Button-1>", add_to_num)
b1.bind("<Button-1>", add_to_num)
b2.bind("<Button-1>", add_to_num)
b3.bind("<Button-1>", add_to_num)
b4.bind("<Button-1>", add_to_num)
b5.bind("<Button-1>", add_to_num)
b6.bind("<Button-1>", add_to_num)
b7.bind("<Button-1>", add_to_num)
b8.bind("<Button-1>", add_to_num)
b9.bind("<Button-1>", add_to_num)
c.bind("<Button-1>", clear)

answer_style = tk.Style()
answer_style.configure("BW.TLabel", font=('Arial', 12))

example = tk.Label(w, text="")
example.place(y=0, x=0, width=110)

result = tk.Label(w, text="", style='BW.TLabel')
result.place(y=20, x=0, width=110)

w.mainloop()
