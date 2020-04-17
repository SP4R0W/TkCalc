#Import Tkinter
from tkinter import *

#Declare variables
global firstNumber
firstNumber = None

global secondNumber
secondNumber = None

global result
result = None

global operator
operator = None

#Initialize the window
root = Tk()
root.title("TkCalc")
root.iconbitmap('icon.ico')

#Initialize the Entry window and place it in the grid system.
e = Entry(root)
e.grid(column=0,row=0,columnspan=6)

def add_number(number):
    #Check if number is -
    if number == "-":
        e.insert(0,number)
    else:
        #If the number is a normal number then treat it like a normal number.
        e.insert(END,number)

def add_operator(sign):
    global firstNumber
    global secondNumber
    global operator
    global result

    if sign == "+":
        #Gets the first number and gets the operator.
        firstNumber = e.get()
        e.delete(0,END)
        operator = "+"

    elif sign == "-":
        firstNumber = e.get()
        e.delete(0,END)
        operator = "-"

    elif sign == "*":
        firstNumber = e.get()
        e.delete(0,END)
        operator = "*"

    elif sign == "/":
        firstNumber = e.get()
        e.delete(0,END)
        operator = "/"

    elif sign == "x2":
        firstNumber = e.get()
        e.delete(0,END)
        #Multiplies the first number by the first number and puts it on the screen
        result = float(firstNumber) * float(firstNumber)
        e.insert(END,result)

    elif sign == "%":
        secondNumber = e.get()
        #Calculates the percentage
        perc = float(firstNumber) * float(secondNumber) / 100

        #Checks which operator is it. Only + and - for now
        if operator == "+":
            result = float(firstNumber) + float(perc)
        elif operator == "-":
            result = float(firstNumber) - float(perc)

        e.delete(0,END)
        e.insert(END,result)

    elif sign == "=":
        secondNumber = e.get()
        e.delete(0,END)
        
        #Checks for operators, then prints the result to screen
        if operator == "+":
            result = float(firstNumber) + float(secondNumber)
        elif operator == "-":
            result = float(firstNumber) - float(secondNumber)
        elif operator == "*":
            result = float(firstNumber) * float(secondNumber)
        elif operator == "/":
            result = float(firstNumber) / float(secondNumber)

        e.insert(END,result)
        

def clear(type):
    #If the button is CE then delete only whats on the screen and if not then clear everything.
    if type == "CE":
        e.delete(0,END)
    elif type == "C":
        e.delete(0,END)
        firstNumber = None
        secondNumber = None
        result = None
        operator = None

#Declaring all the buttons and placing them...

buttonPlus = Button(root,text="+",padx=7.5,pady=3,command=lambda:add_operator('+')).grid(column=3,row=5)
buttonMinus = Button(root,text="-",padx=7.5,pady=3,command=lambda:add_operator('-')).grid(column=3,row=4)
buttonMul = Button(root,text="*",padx=7.5,pady=3,command=lambda:add_operator('*')).grid(column=3,row=3)
buttonDiv = Button(root,text="/",padx=7.5,pady=3,command=lambda:add_operator('/')).grid(column=3,row=2)

buttonPow = Button(root,text="x2",padx=7.5,pady=3,command=lambda:add_operator('x2')).grid(column=1,row=2)
buttonPerc = Button(root,text="%",padx=7.5,pady=3,command=lambda:add_operator('%')).grid(column=0,row=2)

buttonEqual = Button(root,text="=",bg='red',padx=7.5,pady=3,command=lambda:add_operator('=')).grid(column=3,row=6)

buttonDel = Button(root,text="C",padx=60,pady=3,command=lambda:clear("C")).grid(column=0,row=1,columnspan=6)
buttonClear = Button(root,text="CE",padx=7.5,pady=3,command=lambda:clear("CE")).grid(column=2,row=2)

buttonOne = Button(root,text="1",padx=7.5,pady=3,command=lambda:add_number("1")).grid(column=0,row=3)
buttonTwo = Button(root,text="2",padx=7.5,pady=3,command=lambda:add_number("2")).grid(column=1,row=3)
buttonThree = Button(root,text="3",padx=7.5,pady=3,command=lambda:add_number("3")).grid(column=2,row=3)

buttonFour = Button(root,text="4",padx=7.5,pady=3,command=lambda:add_number("4")).grid(column=0,row=4)
buttonFive = Button(root,text="5",padx=7.5,pady=3,command=lambda:add_number("5")).grid(column=1,row=4)
buttonSix = Button(root,text="6",padx=7.5,pady=3,command=lambda:add_number("6")).grid(column=2,row=4)

buttonSeven = Button(root,text="7",padx=7.5,pady=3,command=lambda:add_number("7")).grid(column=0,row=5)
buttonEight = Button(root,text="8",padx=7.5,pady=3,command=lambda:add_number("8")).grid(column=1,row=5)
buttonNine = Button(root,text="9",padx=7.5,pady=3,command=lambda:add_number("9")).grid(column=2,row=5)

buttonPlusMinus = Button(root,text="±",padx=7.5,pady=3,command=lambda:add_number("-")).grid(column=0,row=6)
buttonZero = Button(root,text="0",padx=7.5,pady=3,command=lambda:add_number("0")).grid(column=1,row=6)
buttonComma = Button(root,text=".",padx=7.5,pady=3,command=lambda:add_number(".")).grid(column=2,row=6)

#Starting the mainloop; aka the whole program
root.mainloop()
