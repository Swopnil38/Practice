from tkinter import*
window = Tk()
window.geometry("600x400")
firstname = Label(window,text="First Name: ")
firstname_input = Entry(window)
lastname = Label(window,text="Last Name: ")
lastname_input = Entry(window)
email = Label(window,text="Email: ")
email_input = Entry(window)
password = Label(window,text="Password: ")
password_input = Entry(window)
confirm_password = Label(window,text="Confirm Password: ")
confirm_password_input = Entry(window)

Login = Button(window,text="Register")
Cancel = Button(window,text="Cancel")


firstname.place(x=0,y=0)
firstname_input.place(x=110,y=0)
lastname.place(x=0,y=25)
lastname_input.place(x=110,y=25)
email.place(x=0,y=50)
email_input.place(x=110,y=50)
password.place(x=0,y=75)
password_input.place(x=110,y=75)
confirm_password.place(x=0,y=100)
confirm_password_input.place(x=110,y=100)

Login.place(x=115,y=125)
Cancel.place(x=175,y=125)


window.mainloop()