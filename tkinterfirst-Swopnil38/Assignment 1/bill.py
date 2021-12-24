from tkinter import*
window = Tk()
window.geometry("600x400")

Item_name = Label(window,text="Item Name : ").place(x = 5,y=20)
item_input = Entry(window,width = 15).place(x=90,y=20)
Item_id = Label(window,text="Item Id : ").place(x = 5,y=50)
item_id_input = Entry(window,width = 15).place(x=90,y=50)
Item_quantity = Label(window,text="Quantity : ").place(x = 5,y=80)
item_quantity_input = Entry(window,width = 15).place(x=90,y=80)
Item_price = Label(window,text="Price : ").place(x = 5,y=110)
item_price_input = Entry(window,width = 15).place(x=90,y=110)

add_item = Button(window,text = "Add Item",padx=5,pady=5).place(x = 10,y=160)
checkout = Button(window,text = "Checkout",padx=5,pady=5).place(x = 90,y=160)

window.mainloop()