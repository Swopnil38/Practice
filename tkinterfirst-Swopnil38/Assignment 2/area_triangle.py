from tkinter import*
#Created Window
window = Tk()
#Made Window Geometry
window.geometry("600x400")
#Gave user to input what
rad = Label(window,text = "Enter Base of Circle:").place(x = 0,y = 0)
#gave Place to take User Input
rad_input = Entry(window,width = 10)
#Placed rad_input to (130,0)
rad_input.place(x = 130,y=0)
#Asked USer to Input Height of circle
rad2 = Label(window,text = "Enter Height of Circle:").place(x = 0,y = 30)
#Taken Input of height of circle
rad2_input = Entry(window,width = 10)
rad2_input.place(x = 130,y=30)
#function to Calculate area
def area():
    #stored Base value in b
    b = float(rad_input.get())
    #stored Height value in h
    h = float(rad2_input.get())
    #calculated Area using area = (1/2)*BAse*Height
    a = (1/2)*b*h
    ar = "Area of Triangle is : " + str(a)
    #display the Area
    are = Label(window,text=str(ar)).place(x = 55,y = 110)
#Button to start calculating area
Area = Button(window,text="Area",padx=5,pady=5,command=area).place(x=50,y = 70)

window.mainloop()