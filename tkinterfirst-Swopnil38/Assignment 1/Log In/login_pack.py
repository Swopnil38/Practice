from tkinter import*
window = Tk()
window.geometry("600x400")
username = Label(window,text="Username: ")
username_input = Entry(window)

password = Label(window,text="Password: ")
password_input = Entry(window)


Login = Button(window,text="Login")
Cancel = Button(window,text="Cancel")


username.pack()
username_input.pack()

password.pack()
password_input.pack()

Login.pack()
Cancel.pack()


window.mainloop()