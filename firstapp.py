import tkinter as tk
from tkinter import *
import random
window = tk.Tk()
window.title("Restaurant Billing")
window.geometry("890x580+0+0")
# window.resizable(False,False)
# my_label = tk.Label(window, text="First Desktop Application").place(x=100, y=100)
# my_button = tk.Button(window, text="click here", bg='red',fg='yellow', activebackground='blue',activeforeground='green').place(relx=0.5, rely=0.5, anchor=tk.CENTER)
Tops = Frame(window,bg="white",width = 1600,height=50,relief=tk.RAISED)
Tops.pack(side=tk.TOP)

f1 = Frame(window,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(window ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)


#----------------------------- top heading --------------------------------------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text=" KVN HOTEL BILLING ",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

def loat(value):
    try:
        return float(value)
    except ValueError:
        return 0.0

def ref():
	x = random.randint(10000,99999)
	randref = str(x)
	rand.set(randref)

	cob = loat(Biryani.get())
	cof = loat(Fries.get())
	cop = loat(Pizza.get())
	cub = loat(Burger.get())
	coc = loat(Coke.get())

	costofbiryani = cob*150
	costodfries = cof*200
	costofpizza = cop*200
	cosrofburger = cob*120
	costofcoke = coc*30


	totalcost = "₹",str('%.2f' %(costofbiryani+costodfries+costofpizza+cosrofburger+costofcoke))
	handlingfee = ((costofbiryani+costodfries+costofpizza+cosrofburger+costofcoke)/99)
	totalcostitems = (costofbiryani+costodfries+costofpizza+cosrofburger+costofcoke)
	gst = ((costofbiryani+costodfries+costofpizza+cosrofburger+costofcoke)*0.05)
	topay = round((totalcostitems+handlingfee+gst))
	Service="₹",str('%.2f'% handlingfee)
	OverAllCost="₹",str(round(totalcostitems+handlingfee+gst))
	PaidTax="₹",str(gst)

	cost.set(totalcost)
	handling_fee.set(Service)
	gst_services.set(PaidTax)
	total.set(OverAllCost)


def dexit():
	window.destroy()

def reset():
	rand.set("")
	Biryani.set("")
	Fries.set("")
	Pizza.set("")
	Burger.set("")
	Coke.set("")
	cost.set("")
	handling_fee.set("")
	gst_services.set("")
	total.set("")


rand = StringVar()
Biryani = StringVar()
Fries = StringVar()
Pizza = StringVar()
Burger = StringVar()
Coke = StringVar()
cost = StringVar()
handling_fee = StringVar()
gst_services = StringVar()
total = StringVar()


lblorder = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="brown",bd=20,anchor='w')
lblorder.grid(row=0,column=0)
txtorder = Entry(f1,font=('aria', 15,'bold'),textvariable=rand, bd=6, insertwidth = 6, bg = 'green',justify = 'right',state='readonly')
txtorder.grid(row=0,column=1)

lblbiryani = Label(f1, font=('aria',16,'bold'),text="Biryani.",fg='brown',bd=20,anchor='w')
lblbiryani.grid(row=1,column=0)
txtbiryani = Entry(f1, font=('aria',15,'bold'),textvariable=Biryani,bd=6,insertwidth = 6, bg='white', justify='right')
txtbiryani.grid(row=1,column =1)

lblfries = Label(f1, font =('aria',16,'bold'), text ="Fries.",fg='brown',bd = 20,anchor='w')
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('aria',15,'bold'),textvariable=Fries,bd=6,insertwidth=6,bg='white',justify='right')
txtfries.grid(row=2,column=1)

lblpizza = Label(f1, font =('aria',16,'bold'), text ="Pizza.",fg='brown',bd = 20,anchor='w')
lblpizza.grid(row=3,column=0)
txtpizza = Entry(f1,font=('aria',15,'bold'),textvariable=Pizza,bd=6,insertwidth=6,bg='white',justify='right')
txtpizza.grid(row=3,column=1)

lblburger = Label(f1, font =('aria',16,'bold'), text ="Burger.",fg='brown',bd = 20,anchor='w')
lblburger.grid(row=4,column=0)
txtburger = Entry(f1,font=('aria',15,'bold'),textvariable=Burger,bd=6,insertwidth=6,bg='white',justify='right')
txtburger.grid(row=4,column=1)

lblcoke = Label(f1, font =('aria',16,'bold'), text ="Coke.",fg='brown',bd = 20,anchor='w')
lblcoke.grid(row=5,column=0)
txtcoke = Entry(f1,font=('aria',15,'bold'),textvariable=Coke,bd=6,insertwidth=6,bg='white',justify='right')
txtcoke.grid(row=5,column=1)


lblcost = Label(f1, font =('aria',16,'bold'), text ="Cost.",fg='black',bd = 20,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('aria',15,'bold'),textvariable=cost,bd=6,insertwidth=6,bg='white',justify='right')
txtcost.grid(row=2,column=3)

lblhandling = Label(f1, font =('aria',16,'bold'), text ="Handling Fee.",fg='black',bd = 20,anchor='w')
lblhandling.grid(row=3,column=2)
txthandling = Entry(f1,font=('aria',15,'bold'),textvariable=handling_fee,bd=6,insertwidth=6,bg='white',justify='right')
txthandling.grid(row=3,column=3)

lblgst = Label(f1, font =('aria',16,'bold'), text ="GST&Services.",fg='black',bd = 20,anchor='w')
lblgst.grid(row=4,column=2)
txtgst = Entry(f1,font=('aria',15,'bold'),textvariable=gst_services,bd=6,insertwidth=6,bg='white',justify='right')
txtgst.grid(row=4,column=3)

lbltotal = Label(f1, font =('aria',16,'bold'), text ="To Pay.",fg='green',bd = 20,anchor='w')
lbltotal.grid(row=5,column=2)
txttotal = Entry(f1,font=('aria',15,'bold'),textvariable=total,bd=6,insertwidth=6,bg='white',justify='right', state='readonly')
txttotal.grid(row=5,column=3)

lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=14,pady=5, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="green",command=ref)
btnTotal.grid(row=8, column=1)

btnReset=Button(f1,padx=14,pady=5, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnReset.grid(row=8, column=2)

btnExit=Button(f1,padx=14,pady=5, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="green",command=dexit)
btnExit.grid(row=8, column=3)



def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Biryani", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coke ", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btnprice.grid(row=8, column=0)




window.mainloop()