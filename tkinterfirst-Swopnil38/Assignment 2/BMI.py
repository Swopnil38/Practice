from tkinter import*
window = Tk()
window.geometry("600x400")
rad = Label(window,text = "Enter Mass of Person:").place(x = 0,y = 0)
#taken mass as user Input
rad_input = Entry(window,width = 10)
rad_input.place(x = 130,y=0)
rad2 = Label(window,text = "Enter Height of Person:").place(x = 0,y = 30)
#Taken User Input of HEight
rad2_input = Entry(window,width = 10)
rad2_input.place(x = 130,y=30)
#Function to calculate BMI
def area():
    #stored mass in m
    m = float(rad_input.get())
    #stored Height in h
    h = float(rad2_input.get())
    #calculated BMI using BMI = mass / Height^2
    a = m/(h*h)
    ar = "BMI of Person is : " + str(a)
    #shown BMI to the User
    are = Label(window,text=str(ar)).place(x = 55,y = 110)
#button to calculate BMI
Area = Button(window,text="Area",padx=5,pady=5,command=area).place(x=50,y = 70)

window.mainloop()