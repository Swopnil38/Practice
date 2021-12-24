from tkinter import*
#Created Window Using Tkinter
window = Tk()
#gave Window a Geometry
window.geometry("600x400")
#asked user to provide USername
username = Label(window,text="Username: ")
#taken userame as Input
username_input = Entry(window)
#asked user to provide password
password = Label(window,text="Password: ")
#Taken passsword as input
password_input = Entry(window)
#Function to show Username after Login Button is Clicked
def show():
    '''Username is stored in a and Later print in cordinated (70,100)'''
    a = username_input.get()
    b = Label(window,text=a)
    b.place(x= 70,y=100)
#Login Button : when pressed username appears
Login = Button(window,text="Login",command=show)
#cancel Button : Notihing happens when pressed
Cancel = Button(window,text="Cancel")

'''Place value for all'''
username.place(x=0,y=0)
username_input.place(x=80,y=0)
password.place(x=0,y=25)
password_input.place(x=80,y=25)
Login.place(x=40,y=50)
Cancel.place(x=105,y=50)


window.mainloop()