from tkinter import*
#created Window using tkinter
window = Tk()
#gave Geometry to Tkinter Window
window.geometry("600x400")
#asked USer to Input Principle
principle = Label(window,text="Principle : ").place(x = 5,y = 5)
#taken principle as input
principle_input = Entry(window,width = 15)
principle_input.place(x = 75,y = 5)
#asked USer to input TIme
time = Label(window,text="Time : ").place(x = 5,y = 35)
#Taken Time as input
time_input = Entry(window,width = 15)
time_input.place(x = 75,y = 35)
#Asked User to Input rate
rate = Label(window,text="Rate : ").place(x = 5,y = 70)
#taken Rate as Input from User
rate_input = Entry(window,width = 15)
rate_input.place(x = 75,y = 70)
#function to calculate Simple Intrest
def si():
    '''Stored Value of Principle,rate & TIme in p,r&t respectively'''
    p = int(principle_input.get())
    t = int(time_input.get())
    r = int(rate_input.get())
    #calculated S.I. and stored value in simple
    simple = (p*t*r)/100
    output = "Simple Intrest : " + str(simple)
    #gave USer the value of S.I.
    out = Label(window,text=output).place (x = 65,y = 130)
#Button to calculate Simple Intrest
Simle_intrest = Button(window,text="Simple Intrest",padx=3,pady=3,command=si).place(x=45,y = 100)
window.mainloop()