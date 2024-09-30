from tkinter import *

root = Tk()
root.title('Sua Calculadora')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

firstNum = ''
divisao = FALSE
multiply = FALSE
add = FALSE
subt = FALSE


root.configure(background='#191970')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#DAA520', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row= 0,
    column=0,
    columnspan=4,
    pady=2
)

#operations and functions
def but_click(num):
    e.insert(END, num)
def but_divide():
    global firstNum
    global divisao
    divisao = TRUE
    firstNum = e.get()
    e.delete(0, END)
def but_sum():
    global firstNum
    global add
    add = TRUE
    firstNum = e.get()
    e.delete(0, END)
def but_sub():
    global firstNum
    global subt
    subt = TRUE
    firstNum = e.get()
    e.delete(0, END)
def but_mult():
    global firstNum
    global multiply
    multiply = TRUE
    firstNum = e.get()
    e.delete(0, END)
def but_c():
    e.delete(0, END)
def but_equal():
    global subt
    global add
    global multiply
    global divisao
    secNumb = e.get()
    e.delete(0, END)
    if add == TRUE:
        e.insert(0, int(firstNum) + int(secNumb))
        add = FALSE
    if subt == TRUE:
        e.insert(0, int(firstNum) - int(secNumb))
        subt = FALSE
    if multiply == TRUE:
        e.insert(0, int(firstNum) * int(secNumb))
        multiply = FALSE
    if divisao == TRUE:
        e.insert(0, int(firstNum) / int(secNumb))
        divisao = FALSE

divide = Button(root,
                text='÷',
                padx=40,
                pady=20,
                command=but_divide,
                relief=FLAT,
                font=('futura', 12, 'bold'),    
)
divide.grid(row=0, column=4)

sum = Button(root,
            text='+',
            padx=46.5,
            pady=20,
            command=but_sum,
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
sum.grid(row=1, column=4)

sub = Button(root,
            text='-',
            padx=48.5,
            pady=20,
            command=but_sub,
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
sub.grid(row=2, column=4)

mult = Button(root,
            text='*',
            padx=48,
            pady=20,
            command=but_mult,
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
mult.grid(row=3, column=4)

c = Button(root,
            text='C',
            padx=45,
            pady=20,
            command=but_c,
            relief=FLAT,
            font=('futura', 13, 'bold'),
            justify=CENTER      
)
c.grid(row=4, column=3)

equal = Button(root,
            text='=',
            padx=47,
            pady=20,
            command=but_equal,
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
equal.grid(row=4, column=4)

#Number-rows
seven = Button(root,
            text='7',
            padx=40,
            pady=20,
            command=lambda: but_click(7),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
seven.grid(row=1, column=1)

eight = Button(root,
            text='8',
            padx=42.5,
            pady=20,
            command=lambda: but_click(8),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
eight.grid(row=1, column=2)

nine = Button(root,
            text='9',
            padx=47,
            pady=20,
            command=lambda: but_click(9),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
nine.grid(row=1, column=3)

four = Button(root,
            text='4',
            padx=40,
            pady=20,
            command=lambda: but_click(4),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
four.grid(row=2, column=1)

five = Button(root,
            text='5',
            padx=42.5,
            pady=20,
            command=lambda: but_click(5),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
five.grid(row=2, column=2)

six = Button(root,
            text='6',
            padx=47,
            pady=20,
            command=lambda: but_click(6),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
six.grid(row=2, column=3)

one = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: but_click(1),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
one.grid(row=3, column=1)

two = Button(root,
            text='2',
            padx=42.5,
            pady=20,
            command=lambda: but_click(2),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
two.grid(row=3, column=2)

three = Button(root,
            text='3',
            padx=47,
            pady=20,
            command=lambda: but_click(3),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
three.grid(row=3, column=3)

zero = Button(root,
            text='0',
            padx=40,
            pady=20,
            command=lambda: but_click(0),
            relief=FLAT,
            font=('futura', 12, 'bold'),
            justify=CENTER      
)
zero.grid(row=4, column=1)

dot = Button(root,
            text='.',
            padx=45.3,
            pady=20,
            command=lambda: but_click('.'),
            relief=FLAT,
            font=('futura', 13, 'bold'),
            justify=CENTER      
)
dot.grid(row=4, column=2)


root.mainloop()