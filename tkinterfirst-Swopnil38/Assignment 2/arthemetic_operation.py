from tkinter import*
'''This Program only perform arthemetic operation of 2 Numbers and doesnot perform arthemetic opertaion
of more than 2 Numbers'''
#created Window from Tkinter
window = Tk()
#Gave size to window
window.geometry("600x400")
#DIsplayed USer what to input
num1 = Label(window,text="Enter The First Number : ")
num1.place(x = 10,y = 20)
#taken 1st Number from user as input
num1_input = Entry(window)
num1_input.place(x = 180,y = 20)
#displayed USer to input Second Number
num2 = Label(window,text="Enter The Second Number : ")
num2.place(x = 10,y = 50)
#Taken 2nd Number as input from USer
num2_input = Entry(window)
num2_input.place(x = 180,y = 50)
#function to add 2 Numbers
def Add():
    '''a stores num1 and b stores num 2 and c calculates num1 + num2 and show result to user'''
    a = int(num1_input.get())
    b = int(num2_input.get())
    c = a+b
    sum = "The Sum of " + str(a) +" & " + str(b)+" is: "+ str(c)
    output = Label(window,text=sum)
    output.place(x = 80, y = 130)
#Function to calculate Subtraction
def Sub():
    '''a stores num1 and b stores num 2 and c calculates num1 - num2 or num2  num 1 which is greater
    and show result to user'''
    a = int(num1_input.get())
    b = int(num2_input.get())
    if a>b:
        c = a-b
        sub = "The Difference of " + str(a) +" & " + str(b)+" is: "+ str(c)
        output = Label(window,text=sub)
    else:
        c = b-a
        sub = "The Difference of " + str(b) +" & " + str(a)+" is: "+ str(c)
        output = Label(window,text=sub)
    output.place(x = 80, y = 150)
#Function to calculate Multiplication
def Mul():
    '''a stores num1 and b stores num 2 and c calculates num1 * num2 and show result to user'''
    a = int(num1_input.get())
    b = int(num2_input.get())
    c = a*b
    mult = "The Multiplication of " + str(a) +" & " + str(b)+" is: "+ str(c)
    output = Label(window,text=mult)
    output.place(x = 80, y = 170)
#Function to calculate Division
def Div():
    '''a stores num1 and b stores num 2 and c calculates num1 / num2 and show result to user'''
    a = int(num1_input.get())
    b = int(num2_input.get())
    c = a/b
    divi = "The Division of " + str(a) +" & " + str(b)+" is: "+ str(c)
    output = Label(window,text=divi)
    output.place(x = 80, y = 190)
#Button To add 2 Number
add = Button(window,text="Add",command=Add)
#Button To sub 2 Number
sub = Button(window,text="Subtract",command=Sub)
#Button To mul 2 Number
mul = Button(window,text="Multiplication",command=Mul)
#Button To div 2 Number
div = Button(window,text="Division",command=Div)


add.place(x=20,y=80)
sub.place(x=60,y=80)
mul.place(x = 120,y = 80)
div.place(x = 210,y = 80)

window.mainloop()