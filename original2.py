import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random
import re

conn = sqlite3.connect("Database\store.db")
c = conn.cursor()

#date
date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
#temporary list like section
products_list = []
product_price = []
product_quantity = []
product_discount = []
product_id = []

#list for labels
labels_list = []



class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches

        
        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList
        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        
        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True
                
                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
        
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != '0':                
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != END:                        
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index) 

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]



class Win1:

    def __init__(self, master, *args, **kwargs):
        
        self.master = master
        #self.master = master 
        autocompleteList = ['Ipad Air', 'Ipad 10.2', 'Watch SE', 'Watch Series 6 Aluminum', 'Watch Series 6', 'Watch Edition Series 6', 'Iphone SE(2020)', 'Ipad Pro 12.9(2020)', 'Ipad Pro 11(2020)', 'Iphone 11 Pro Max', 'Iphone 11 Pro', 'Iphone 11', 'Ipad 10.2(2019)', 'Watch Edition Series 5', 'Watch Series 5', 'Watch Series 5 Aluminum', 'Ipad Air(2019)', 'Ipad Mini(2019)', 'Ipad Pro 12.9 (2018)', 'Ipad Pro 11(2018)', 'Iphone XS Max', 'Iphone XS', 'Iphone XR', 'Watch Series 4', 'Watch Series 4 Aluminum', 'Ipad 9.7(2018)', 'Iphone X', 'Iphone 8 Plus', 'Iphone 8', 'Ipad Pro 12.9(2017)', 'Iphone 7 Plus', 'Iphone 7', 'Iphone SE', 'Iphone 6s Plus', 'Iphone 6s', 'Iphone 6s Plus', 'Iphone 6', 'Iphone 5s', 'Iphone 5c', 'Iphone 5', 'Iphone 4s', 'Iphone 4', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)' ]
        # autocompleteList.append(Win2.call)

        query = "SELECT name FROM inventory"
        result = c.execute(query)
        for self.u in result:
            autocompleteList.append(self.u)
        def matches(fieldValue, acListEntry):
            pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
            return re.match(pattern, str(acListEntry))
        self.master.geometry("1366x768+0+0")
        self.show_widgets()

        self.left = Frame(master, width=800, height=768, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=566, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)

                #components
        self.heading = Label(master, text= "Latest Technologies    ", font=('arial 40 bold'), bg='white')
        self.heading.place(x=0, y=0)

        self.date_l = Label(self.right, text="Today's Date: "+str(date), font=('arial 14 bold'), bg='lightblue', fg='white')
        self.date_l.place(x=0, y=0)

        

        # self.time_l = Label(self.right, text="Time: "+str(datetime.datetime.now().strftime("%H:%M:%S")), font=('arial 14 bold'), bg='lightblue', fg='white')
        # self.time_l.place(x=300, y=0)


        #table invoice=========================
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=60)
        
        self.tquantity = Label(self.right, text="quantity", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=200, y=60)

        self.tamount = Label(self.right, text="amount", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tamount.place(x=400, y=60)

        #enter stuff
        self.enterid = Label(self.left, text="Enter Product's ID", font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=260, y=80)
        self.enteride.focus()

        self.entername = Label(self.left, text="Enter Product's Name", font=('arial 18 bold'), bg='white')
        self.entername.place(x=0, y=150)

        self.entername_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.entername_e.place(x=260, y=150)

        #Autocomplete Entry
        self.entername_e = AutocompleteEntry(autocompleteList, master, listboxLength=10, width=25, font=('arial 18 bold'), bg='lightblue', matchesFunction=matches)
        self.entername_e.place(x=260, y=175)

        #button 
        self.search_btn = Button(self.left, text="Search by Id", width=20, height=2, bg='orange', command=self.ajax1)
        self.search_btn.place(x=600, y=80)

        self.search_btn = Button(self.left, text="Search by Name", width=20, height=2, bg='orange', command=self.ajax2)
        self.search_btn.place(x=600, y=150)

        self.clear_btn = Button(self.left, text="Clear All", width=20, height=2, bg='green', fg='white', command=self.clear)
        self.clear_btn.place(x=600, y=490)

        #fill it later by the fucntion ajax
        self.productname = Label(self.left, text="", font=('arial 25 bold'), bg='white', fg='green')
        self.productname.place(x=0, y=210)

        self.pprice = Label(self.left, text="", font=('arial 25 bold'), bg='white', fg='green')
        self.pprice.place(x=0, y=250)

        self.pbrand = Label(self.left, text="", font=('arial 25 bold'), bg='white', fg='green')
        self.pbrand.place(x=0, y=290)

        self.pstock = Label(self.left, text="", font=('arial 25 bold'), bg='white', fg='green')
        self.pstock.place(x=400, y=290)

        #total label
        self.total_l = Label(self.right, text="Total", font=('arial 40 bold'), bg='lightblue', fg='green')
        self.total_l.place(x=0, y=600)

        self.master.bind('<Return>', self.ajax2)
        #self.master.bind('<Right>', self.ajax1)
        self.master.bind('<F12>', self.add_to_cart)
        #self.master.bind('<shift>', self.generate_bill)

        

    def clear(self, *args, **kwargs):
        for a in labels_list:
            a.destroy()

        del(products_list[:])
        del(product_id[:])
        del(product_quantity[:])
        del(product_discount[:])
        del(product_price[:])

        self.total_l.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()
        


    def ajax2(self, *args, **kwargs):
        self.get_name = self.entername_e.get()
        #get the products info with that name or id and fill labels above
        query = "SELECT * FROM inventory WHERE name=?"
        result = c.execute(query, (self.get_name, ))
        empty = True
        for self.r in result:
            empty = False
            self.get_id = self.r[0]
            self.get_name = self.r[1] #name
            self.get_price = self.r[4] #sp
            self.get_stock = self.r[2] #stock
            self.get_brand = self.r[10] #brand
        #if self.get_name != self.r[1]: or/
        if empty:
            tkinter.messagebox.showinfo("Error","Not in Stock")
        else:
            self.enteride.delete(0, END)
            self.enteride.insert(0, str(self.get_id))
            self.productname.configure(text="Device Name: "+ str(self.get_name))
            self.pprice.configure(text="Price: Gh "+str(self.get_price))
            self.pbrand.configure(text="Brand: "+str(self.get_brand))
            self.pstock.configure(text="Available in stock: "+str(self.get_stock))


            #create quantity and discount label
            self.quantity_l = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg='white')
            self.quantity_l.place(x=0, y=370)

            self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.quantity_e.place(x=190, y=370)
            self.quantity_e.focus()

            #discount
            self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'), bg='white')
            self.discount_l.place(x=0, y=410)
        
            self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.discount_e.place(x=190, y=410)
            self.discount_e.insert(END, 0)
            
            #add to cart
            self.add_to_cart_btn = Button(self.left, text="Add to Cart(F12)", width=20, height=2, bg='orange', command=self.add_to_cart)
            self.add_to_cart_btn.place(x=360, y=450)
            

            #generate bill and change
            self.change_l = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg='white')
            self.change_l.place(x=0, y=550)

            self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.change_e.place(x=190, y=550)

            #button change
            self.change_btn = Button(self.left, text="Calculate Change", width=20, height=2, bg='orange', command=self.change)
            self.change_btn.place(x=360, y=590)

            #generate bill button
            self.bill_btn = Button(self.left, text="Generate Bill", width=45, height=3, bg='red', fg='white', command=self.generate_bill)
            self.bill_btn.place(x=190, y=650)

    def ajax1(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        #get the products info with that name or id and fill labels above
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        empty = True
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1] #name
            self.get_price = self.r[4] #sp
            self.get_stock = self.r[2] #stock
            self.get_brand = self.r[10] #stock
        if self.get_id != self.r[0]:
            tkinter.messagebox.showinfo("Error","Not in Stock")
        else:
            self.entername_e.delete(0, END)
            self.entername_e.insert(0, str(self.get_name))
            self.productname.configure(text="Device Name: "+ str(self.get_name))
            self.pprice.configure(text="Price: Gh "+str(self.get_price))
            self.pbrand.configure(text="Brand: "+str(self.get_brand))
            self.pstock.configure(text="Available in stock: "+str(self.get_stock))



            #create quantity and discount label
            self.quantity_l = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg='white')
            self.quantity_l.place(x=0, y=370)

            self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.quantity_e.place(x=190, y=370)
            self.quantity_e.focus()

            #discount
            self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'), bg='white')
            self.discount_l.place(x=0, y=410)
        
            self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.discount_e.place(x=190, y=410)
            self.discount_e.insert(END, 0)
            
            #add to cart
            self.add_to_cart_btn = Button(self.left, text="Add to Cart(F12)", width=20, height=2, bg='orange', command=self.add_to_cart)
            self.add_to_cart_btn.place(x=360, y=450)
            

            #generate bill and change
            self.change_l = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg='white')
            self.change_l.place(x=0, y=550)

            self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.change_e.place(x=190, y=550)

            #button change
            self.change_btn = Button(self.left, text="Calculate Change", width=20, height=2, bg='orange', command=self.change)
            self.change_btn.place(x=360, y=590)

            #generate bill button
            self.bill_btn = Button(self.left, text="Generate Bill", width=45, height=3, bg='red', fg='white', command=self.generate_bill)
            self.bill_btn.place(x=190, y=650)


        

    def add_to_cart(self, *args, **kwargs):
        #gt the quantity value from the database
        self.discount_value = float(self.discount_e.get())
        self.quantity_value = int(self.quantity_e.get())
        if  self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in Stock.")
        else:
            #calculate the price
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value) 
            product_id.append(self.get_id)
            product_discount.append(self.discount_value)

            print(products_list)
            print(product_price)
            print(product_quantity)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'), bg='lightblue')
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue')
                self.tempqt.place(x=200, y=self.y_index)
                labels_list.append(self.tempqt)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='lightblue')
                self.tempprice.place(x=400, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index += 40
                self.counter += 1

                #total configure
                self.total_l.configure(text="Total: Gh "+ str(sum(product_price)))
                
                #delete
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.pbrand.configure(text="")
                self.pstock.configure(text="")
                #self.entername_e.configure(text="")
                self.add_to_cart_btn.destroy()
                

                #auto focus to enter ID
                self.entername_e.focus()
                self.entername_e.delete(0, END)

    def change(self, *args, **kwargs):
        #get the amount given by the customer and the amount generated by the computer
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        #label change
        self.c_amount = Label(self.left, text="Change: Gh " + str(self.to_give), font=('arial 18 bold'), fg='red', bg='white')
        self.c_amount.place(x=360, y=550)

    def generate_bill(self, *args, **kwargs):
        #create bill before updating the database

        time_l = Label(self.right, text="", font=('arial 14 bold'), bg='lightblue', fg='white')
        time_l.place(x=300, y=0)


        now = datetime.datetime.now()

        if  str(self.change_e.get()) == "":
            tkinter.messagebox.showinfo("Error", "Enter Amount.")
        else:
            directory = "C:/SAMS/invoice/ " + str(date) + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)

            #TEMPLATES FOR THE BILL
            company = "\n\t\t\t\t Latest Technologies."
            address = "\n\t\t\t\t       OSU-ACCRA."
            phone = "\n\t\t\t\t    TEL:0509387222"
            sample = "\n\t\t\t\t        T.I.N #:"
            dt = "\n\t\t\t\t       " + str(date)
            ti = "\n\t\t\t\t        " + str(now.strftime("%H:%M:%S"))
            table_header = "\n\t\t------------------------------------------------- \n\t\t\tSN.\t Products\t\tQty\t\tAmount\n\t\t-------------------------------------------------"
            final = company + address + phone + sample + dt + ti + "\n" + table_header

            #open a file to write to 
            file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
            f=open(file_name, 'w')
            f.write(final)
            #fill dynamics
            r = 0
            for t in products_list:
                f.write("\n\t\t\t" + str(r+1) + "\t" + str(products_list[r]+"......")[:11] + "\t\t" + str(product_quantity[r]) + "\t\t" + str(product_price[r]))
                r +=1
            f.write("\n\n\t\t-------------------------------------------------")
            f.write("\n\t\t\tTotal: Gh " + str(sum(product_price)))
            f.write("\n\t\t\tAmount Paid: Gh " + str(self.change_e.get()))
            f.write("\n\t\t\tDiscount: Gh " + str(sum(product_discount)))
            f.write("\n\t\t\tBalance: Gh " + str((float(self.change_e.get())) - float(sum(product_price))))
            f.write("\n\t\t\tThanks for Shopping with us.")
            f.write("\n\t\t-------------------------------------------------")
            f.write("\n\t\t\t\tSoftware Designed by Tek-divisal")
            f.write("\n\t\t         darkolawrence@gmail.com   0501131739")
            os.startfile(file_name, "print")
            f.close()
            #decrease the stock
            self.x = 0


            initial = "SELECT * FROM inventory WHERE id=?"
            result = c.execute(initial, (product_id[self.x], ))
            
            for i in products_list:
                for r in result:
                    self.old_stock = r[2]
                self.new_stock = int(self.get_stock) - int(product_quantity[self.x])

                #updating stock
                sql = "UPDATE inventory SET stock=? WHERE id=?"
                c.execute(sql, (self.new_stock, product_id[self.x]))
                conn.commit()

                #insert into the transaction table
                sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
                c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x], date))
                conn.commit()
                
                self.x += 1

            for a in labels_list:
                a.destroy()

            del(products_list[:])
            del(product_id[:])
            del(product_quantity[:])
            del(product_discount[:])
            del(product_price[:])

            self.total_l.configure(text="")
            self.c_amount.configure(text="")
            self.change_e.delete(0, END)
            self.enteride.focus()
        
        
            tkinter.messagebox.showinfo("Success", "Done")

    def show_widgets(self, *args, **kwargs):
        self.frame = tk.Frame(self.master)
        self.master.title("Dashboard")
        self.create_button("Add to database", Win2)
        self.create_button("Update database", Win3)
        self.frame.pack()
 
    def create_button(self, text, _class):
        "Button that creates a new window"
        tk.Button(self.frame, text=text, bg='green', fg='white', command=lambda: self.new_window(_class)).pack(side=LEFT, fill=BOTH, padx=0, pady=0, anchor=N)
        
 
    def new_window(self, _class):
        self.win = tk.Toplevel(self.master)
        _class(self.win)
 
 
class Win2(Win1):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title("Add")
        self.master.geometry("1366x768+0+0")
        self.show_widgets()

        self.heading = Label(master, text= "Add to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=50, y=0)

        #labels for the windows
        self.name_l = Label(master, text = "Enter Device Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=80)

        self.brand_l = Label(master, text = "Enter Brand Name", font=('arial 18 bold'))
        self.brand_l.place(x=0, y=150)

        self.stock_l = Label(master, text = "Enter Stock", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=220)

        self.cp_l = Label(master, text = "Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=290)

        self.sp_l = Label(master, text = "Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=350)

        self.vendor_l = Label(master, text = "Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=410)

        self.vendor_num_l = Label(master, text = "Enter Vendor Phone Number", font=('arial 18 bold'))
        self.vendor_num_l.place(x=0, y=460)

        #label Entries
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=350, y=80)

        


        self.brand_e = Entry(master, width=25, font=('arial 18 bold'))
        self.brand_e.place(x=350, y=150)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=350, y=220)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=350, y=280)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=350, y=350)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=350, y=410)

        self.vendor_num_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_num_e.place(x=350, y=460)

        #Button to add to database
        self.btn_add = Button(master, text="Add to Database", width=20, height=2, bg='steelblue', fg='white', command=self.get_items)
        self.btn_add.place(x=350, y=520)

        self.btn_add = Button(master, text="Clear Fields", width=20, height=2, bg='green', fg='white', command=self.clear_all)
        self.btn_add.place(x=520, y=520)

        #Text box for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=74)

        
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)
 
    def clear_all(self, *args, **kwargs):
            #num = id + 1
        self.name_e.delete(0, END)
        self.brand_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_num_e.delete(0, END)

        #Get Data from Entries
    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.brand = self.brand_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_num = self.vendor_num_e.get()
        
    
        if self.name =='' or self.brand =='' or self.stock =='' or self.cp =='' or self.sp =='' :
            tkinter.messagebox.showinfo("Error", "Please Fill the Various Fields")
        else:
            #Dynamic Entries
            self.totalcp = float(self.cp) * float(self.sp)
            self.totalsp = float(self.sp) * float(self.stock)
            self.assumed_profit = float(self.totalsp - self.totalcp)
            
            sql = "INSERT INTO inventory (name, brand, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_num) VALUES(?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.brand, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_num))
            conn.commit()
            
            self.tBox.insert(END, "\n\nInserted " + str(self.name) + " into the database")

        def call_list(self):
            autocompleteList2 = []
            autocompleteList2.append(self.name_e.get())
  

    def show_widgets(self):
        "A frame with a button to quit the window"
        self.frame = tk.Frame(self.master, bg="steelblue")
        self.quit_button = tk.Button(self.frame, text=f"close", bg="red", fg="white", command=self.close_window)
        self.quit_button.pack(side="left", fill="x", padx=0, pady=0, anchor=N)
        self.create_button("Update Database", Win3)
        self.frame.pack()
 
    def close_window(self):
        self.master.destroy()
 
 
class Win3(Win1):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        
        
        autocompleteList = [ 'Ipad Air', 'Ipad 10.2', 'Watch SE', 'Watch Series 6 Aluminum', 'Watch Series 6', 'Watch Edition Series 6', 'Iphone SE(2020)', 'Ipad Pro 12.9(2020)', 'Ipad Pro 11(2020)', 'Iphone 11 Pro Max', 'Iphone 11 Pro', 'Iphone 11', 'Ipad 10.2(2019)', 'Watch Edition Series 5', 'Watch Series 5', 'Watch Series 5 Aluminum', 'Ipad Air(2019)', 'Ipad Mini(2019)', 'Ipad Pro 12.9 (2018)', 'Ipad Pro 11(2018)', 'Iphone XS Max', 'Iphone XS', 'Iphone XR', 'Watch Series 4', 'Watch Series 4 Aluminum', 'Ipad 9.7(2018)', 'Iphone X', 'Iphone 8 Plus', 'Iphone 8', 'Ipad Pro 12.9(2017)', 'Iphone 7 Plus', 'Iphone 7', 'Iphone SE', 'Iphone 6s Plus', 'Iphone 6s', 'Iphone 6s Plus', 'Iphone 6', 'Iphone 5s', 'Iphone 5c', 'Iphone 5', 'Iphone 4s', 'Iphone 4', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)' ]
        
        def matches(fieldValue, acListEntry):
            pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
            return re.match(pattern, acListEntry)
        self.master.title("Update")
        self.master.geometry("1366x768+0+0")
        self.show_widgets()

        self.heading = Label(master, text= "Update the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=50, y=0)


        #labels for entrie
        self.id_le = Label(master, text="Enter Id", font=('arial 18 bold'))
        self.id_le.place(x=0, y=80)

        self.id_leb = Entry(master, width=15, font=('arial 18 bold'))
        self.id_leb.place(x=350, y=80)

        self.btn_search = Button(master, text="Search Id", width=15, height=2, bg='orange', fg='white', command=self.search1)
        self.btn_search.place(x=565, y=80)

        #labels for the windows
        self.name_l = Label(master, text = "Enter Product Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=130)

        self.brand_l = Label(master, text = "Enter Brand Name", font=('arial 18 bold'))
        self.brand_l.place(x=0, y=180)

        self.stock_l = Label(master, text = "Enter Stock", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=250)

        self.cp_l = Label(master, text = "Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=310)

        self.sp_l = Label(master, text = "Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=370)

        self.totalcp_l = Label(master, text = "Total Cost Price", font=('arial 18 bold'))
        self.totalcp_l.place(x=0, y=440)

        self.totalsp_l = Label(master, text = "Total Selling Price", font=('arial 18 bold'))
        self.totalsp_l.place(x=0, y=510)

        self.vendor_l = Label(master, text = "Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=580)

        self.vendor_num_l = Label(master, text = "Enter Vendor Phone Number", font=('arial 18 bold'))
        self.vendor_num_l.place(x=0, y=650)

        #label Entries
        self.name_e = Entry(master, width=15, font=('arial 18 bold'))
        self.name_e.place(x=350, y=130)

        self.name_e = AutocompleteEntry(autocompleteList, master, listboxLength=10, width=20, font=('arial 18 bold'), matchesFunction=matches)
        self.name_e.place(x=350, y=130)

        self.btn_search = Button(master, text="Search Name", width=15, height=2, bg='orange', fg='white', command=self.search2)
        self.btn_search.place(x=620, y=130)

        self.brand_e = Entry(master, width=25, font=('arial 18 bold'))
        self.brand_e.place(x=350, y=180)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=350, y=250)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=350, y=310)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=350, y=370)

        self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalcp_e.place(x=350, y=440)

        self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalsp_e.place(x=350, y=510)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=350, y=580)

        self.vendor_num_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_num_e.place(x=350, y=650)

        #Button to update the database
        self.btn_add = Button(master, text="Update Database", width=20, height=2, bg='green', fg='white', command=self.update)
        self.btn_add.place(x=440, y=690)


        #Text box for the logs
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x=750, y=74)

    def search1(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result: 
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp
            self.n7 = r[7] #assumed_profit
            self.n8 = r[8] #vendor
            self.n9 = r[9] #vendor_phone
            self.n10 = r[10] #brand
        conn.commit()

        #insert into the entries to update
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_num_e.delete(0, END)
        self.vendor_num_e.insert(0, str(self.n9))

        self.brand_e.delete(0, END)
        self.brand_e.insert(0, str(self.n10))

    def search2(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE name=?"
        result = c.execute(sql, (self.name_e.get(), ))
        for r in result: 
            self.n0 = r[0]
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp
            self.n7 = r[7] #assumed_profit
            self.n8 = r[8] #vendor
            self.n9 = r[9] #vendor_phone
            self.n10 = r[10] #brand
        conn.commit()

        #insert into the entries to update
        self.id_leb.delete(0, END)
        self.id_leb.insert(0, str(self.n0))

        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_num_e.delete(0, END)
        self.vendor_num_e.insert(0, str(self.n9))

        self.brand_e.delete(0, END)
        self.brand_e.insert(0, str(self.n10))

    def update(self, *args, **kwargs):
        #get all the updated values
        self.u0 = self.id_leb.get()
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_num_e.get()
        self.u9 = self.brand_e.get()




        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_num=?, brand=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.u9, self.u0))
        conn.commit()
        tkinter.messagebox.showinfo("Success","Database Updated")
        self.tBox.insert(END, "You just updated " + self.name_e.get()+" \n")
 
        

 
    def show_widgets(self):
        self.frame = tk.Frame(self.master, bg="green")
        self.quit = tk.Button(self.frame, text=f"Close", command=self.close_window)
        self.quit.pack()
        #self.label = tk.Label(self.frame, text="THIS IS ONLY IN THE THIRD WINDOW")
        #self.label.pack()
        self.frame.pack()
 
    def close_window(self):
        self.master.destroy()

 
 
root = tk.Tk()
app = Win1(root)
root.iconbitmap('C:\\Users\\GH\\Desktop\\Developments\\Management Sys\\icon.ico')
root.mainloop()