from tkinter import*
window = Tk()
window.geometry("600x400")
username = Label(window,text="Username: ")
username_input = Entry(window)

password = Label(window,text="Password: ")
password_input = Entry(window)


Login = Button(window,text="Register")
Cancel = Button(window,text="Cancel")


username.place(x=0,y=0)
username_input.place(x=80,y=0)

password.place(x=0,y=25)
password_input.place(x=80,y=25)


Login.place(x=40,y=50)
Cancel.place(x=105,y=50)


window.mainloop()