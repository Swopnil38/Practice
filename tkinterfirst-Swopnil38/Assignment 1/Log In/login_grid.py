from tkinter import*
window = Tk()
window.geometry("600x400")
Username = Label(window,text="Username: ")
Username_input = Entry(window)
password = Label(window,text="Password: ")
password_input = Entry(window)


Login = Button(window,text="Log In")
Cancel = Button(window,text="Cancel")


Username.grid(row=0,column=1)
Username_input.grid(row=0,column=3)
password.grid(row=3,column=1)
password_input.grid(row=3,column=3)


Login.grid(row=15,column=2)
Cancel.grid(row=15,column=3)


window.mainloop()