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


firstname.pack()
firstname_input.pack()
lastname.pack()
lastname_input.pack()
email.pack()
email_input.pack()
password.pack()
password_input.pack()
confirm_password.pack()
confirm_password_input.pack()

Login.pack()
Cancel.pack()


window.mainloop()