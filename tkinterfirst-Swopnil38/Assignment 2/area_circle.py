from tkinter import*
#Created Window
window = Tk()
#Made Geometry Size as 600 X 400
window.geometry("600x400")
#Text to User to input what
rad = Label(window,text = "Enter Area of Circle:").place(x = 0,y = 0)
#Place to Take input from user
rad_input = Entry(window,width = 10)
#Placed at (130,0)
rad_input.place(x = 130,y=0)
#function to calculate area
def area():
    #stored value taken from user to r
    r = float(rad_input.get())
    #Calculated Area of circle
    a = (22/7)*r*r
    #Stored Text of Output to ar
    ar = "Area of Circle is : " + str(a)
    #Showed Area of Triangle to User
    are = Label(window,text=str(ar)).place(x = 55,y = 110)
#Button to calculate area
# Direct to function area after button is clicked
Area = Button(window,text="Area",padx=5,pady=5,command=area).place(x=50,y = 40)
#Packed all
window.mainloop()