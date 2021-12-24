from tkinter import*
#Created Window
window = Tk()
#Made Geometry Size as 600 X 400
window.geometry("600x400")
#Text to User to input what
edg = Label(window,text = "Enter Edge of cube:").place(x = 0,y = 0)
#Place to Take input from user
edg_input = Entry(window,width = 10)
#Placed at (130,0)
edg_input.place(x = 130,y=0)
#function to calculate volume of cube
def volume():
    #stored value taken from user to e
    e = float(edg_input.get())
    #Calculated Area of circle
    v = e*e*e
    #Stored Text of Output to vo
    vo= "Volume of Cube is : " + str(v)
    #Showed Volume of Cube to User
    vol = Label(window,text=str(vo)).place(x = 55,y = 110)
#Button to calculate volume
# Direct to function Volume after button is clicked
Volume = Button(window,text="Volume",padx=5,pady=5,command=volume).place(x=50,y = 40)
#Packed all
window.mainloop()