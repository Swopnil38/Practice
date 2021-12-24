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

Login = Button(window,text="Log In")
Cancel = Button(window,text="Cancel")


firstname.grid(row=0,column=1)
firstname_input.grid(row=0,column=3)
lastname.grid(row=3,column=1)
lastname_input.grid(row=3,column=3)
email.grid(row=5,column=1)
email_input.grid(row=5,column=3)
password.grid(row=7,column=1)
password_input.grid(row=7,column=3)+
confirm_password.grid(row=9,column=1)
confirm_password_input.grid(row=9,column=3)

Login.grid(row=15,column=2)
Cancel.grid(row=15,column=3)


window.mainloop()