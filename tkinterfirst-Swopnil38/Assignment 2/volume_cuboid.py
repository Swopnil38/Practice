from tkinter import*
#Created Window
window = Tk()
#Made Window Geometry
window.geometry("600x400")
#Gave user to input what
len = Label(window,text = "Enter Length of Cuboid:").place(x = 0,y = 0)
#gave Place to take User Input
len_input = Entry(window,width = 10)
#Placed len_input to (130,0)
len_input.place(x = 130,y=0)
#Asked USer to Input Height of cuboid
hei = Label(window,text = "Enter Height of Cuboid:").place(x = 0,y = 30)
#Taken Input of height of circle
hei_input = Entry(window,width = 10)
hei_input.place(x = 130,y=30)
#Asked USer to Input Width of cuboid
wid = Label(window,text = "Enter Width of Cuboid:").place(x = 0,y = 60)
#Taken Input of height of circle
wid_input = Entry(window,width = 10)
wid_input.place(x = 130,y=60)

#function to Calculate volume of cuboid
def Volume():
    #stored length value in l
    l = float(len_input.get())
    #stored Height value in h
    h = float(hei_input.get())
    # stored Width value in w
    w = float(wid_input.get())
    #calculated volume of cuboid = length*width*Height
    v = l*w*h
    vo = "Volume of Cuboid is : " + str(v)
    #display the Area
    vol = Label(window,text=str(vo))
    vol.place(x = 55,y = 130)
#Button to start calculating area
volume = Button(window,text="Volume",padx=5,pady=5,command=Volume).place(x=50,y = 90)

window.mainloop()