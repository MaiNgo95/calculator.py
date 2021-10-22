from tkinter import*

def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator =''
    text_input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=" "

cal = Tk()
cal.title("Calculator")
operator =""
text_input = StringVar()
textDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable= text_input, bd=30, insertwidth=4, bg='aquamarine', justify='right').grid(columnspan=4)

#justify mean get the input from the right
#bd get the size of the box

btn7 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'),
             text='7', command=lambda:btnClick(7), bg="powder blue").grid(row=1, column= 0)
btn8 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'),
             text='8', command=lambda:btnClick(8),bg ="powder blue").grid(row=1, column= 1)
btn9 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='9',command=lambda:btnClick(9),bg ="powder blue").grid(row=1, column= 2)
additional=Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='+',command=lambda:btnClick("+"),bg ="powder blue").grid(row=1, column= 3)
btn4 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='4',command=lambda:btnClick(4),bg ="powder blue").grid(row=2, column= 0)
btn5 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='5',command=lambda:btnClick(5),bg ="powder blue").grid(row=2, column= 1)
btn6 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='6',command=lambda:btnClick(6),bg ="powder blue").grid(row=2, column= 2)
subtraction=Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='-',command=lambda:btnClick('-'),bg ="powder blue").grid(row=2, column= 3)
btn1 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='1',command=lambda:btnClick(1),bg ="powder blue").grid(row=3, column= 0)
btn2 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='2',command=lambda:btnClick(2),bg ="powder blue").grid(row=3, column= 1)
btn3 =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='3',command=lambda:btnClick(3),bg ="powder blue").grid(row=3, column= 2)
multiple=Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='*',command=lambda:btnClick('*'),bg ="powder blue").grid(row=3, column= 3)
clear =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='A/C',command=btnClear,bg ="powder blue").grid(row=4, column= 1)
equal =Button(cal, padx=16, pady=16, bd=8,fg='deep pink',font=('arial',20, 'bold'), text='=',command=btnEqual,bg ="powder blue").grid(row=4, column= 2)
division =Button(cal, padx=16, pady=16,bd=8, fg='deep pink',font=('arial',20, 'bold'), text='/',command=lambda:btnClick('/'),bg ="powder blue").grid(row=4, column= 3)
btn0=Button(cal, padx=16, pady=16, fg='deep pink',font=('arial',20, 'bold'), text='0',command=lambda:btnClick(0),bg ="powder blue").grid(row=4, column= 0)

#pady=16
#fg: foreground get the ground color
#grid use to get the position of the button in the table
cal.mainloop()
