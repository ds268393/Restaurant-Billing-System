from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.ttk import Combobox,Treeview,Style
import random
import gmail
from sqlite3 import *
from datetime import datetime

win=Tk()
win.state("zoomed")
win.configure(bg='skyblue')
win.resizable(width=False,height=False)

title_lbl=Label(win,text='Restaurant Billing System',font=('',55,'bold','underline'),bg='skyblue')
title_lbl.place(relx=.2,rely=.05)

img1=PhotoImage(file="logo1.png")
img2=PhotoImage(file="logo2.png")

logo_lbl1=Label(win,image=img1)
logo_lbl1.place(x=0,y=0)

logo_lbl2=Label(win,image=img2)
logo_lbl2.place(relx=.85,y=0)


def home_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    user_label=Label(frm,text="Username",font=('',20,'bold'),bg='pink')
    user_entry=Entry(frm,font=('',20,'bold'),bd=10)
    user_entry.focus()

    pass_label=Label(frm,text="Password",font=('',20,'bold'),bg='pink')
    pass_entry=Entry(frm,show="*",font=('',20,'bold'),bd=10)
    
    
    login_btn=Button(frm,command=lambda:auth(),width=8,text="login",font=('',20,'bold'),bd=10)
    reset_btn=Button(frm,command=lambda:reset_home(),width=8,text="reset",font=('',20,'bold'),bd=10)

    user_label.place(relx=.3,rely=.2)
    user_entry.place(relx=.45,rely=.2)
    
    pass_label.place(relx=.3,rely=.3)
    pass_entry.place(relx=.45,rely=.3)

    login_btn.place(relx=.35,rely=.45)
    reset_btn.place(relx=.5,rely=.45)
    
    def reset_home():
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        user_entry.focus()

    def auth():
        u=user_entry.get()
        p=pass_entry.get()
        if(len(u)==0 or len(p)==0):
            messagebox.showwarning('Validation',"Username/Password cann't be empty")
        else:
            if(u=='admin' and p=='admin'):
                frm.destroy()
                welcome_screen()
            else:
                 messagebox.showerror('Validation',"Invalid Username/Password")


def welcome_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    billing_btn=Button(frm,command=lambda:billing(),width=12,text="Billing",font=('',20,'bold'),bd=10)
    billing_btn.place(relx=.4,rely=.1)

    addItem_btn=Button(frm,command=lambda:addItem(),width=12,text="Add Item",font=('',20,'bold'),bd=10)
    addItem_btn.place(relx=.4,rely=.25)

    editPrice_btn=Button(frm,command=lambda:editPrice(),width=12,text="Edit Price",font=('',20,'bold'),bd=10)
    editPrice_btn.place(relx=.4,rely=.4)

    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()
               
    
    def addItem():
        frm.destroy()
        additem_screen()
    
    def editPrice():
        frm.destroy()
        editprice_screen()
    
    def billing():
        frm.destroy()
        billing_screen()
    
def additem_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    title_lbl=Label(frm,text="Add Item",font=('',50,'bold','italic'),bg='pink',fg='green')
    title_lbl.place(relx=.35,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    back_btn=Button(frm,command=lambda:back(),width=6,text="back",font=('',20,'bold'),bd=10)
    back_btn.place(x=1,y=60)


    item_label=Label(frm,text="Item Name",font=('',20,'bold'),bg='pink')
    item_entry=Entry(frm,font=('',20,'bold'),bd=10)
    item_entry.focus()


    price_label=Label(frm,text="Price/Unit",font=('',20,'bold'),bg='pink')
    price_entry=Entry(frm,font=('',20,'bold'),bd=10)
    
    l_cat=Label(frm,text="Category",font=('',20,'bold'),bg='pink')
    l_cat.place(relx=.3,rely=.4)
    e_cat=Entry(frm,font=('',20,'bold'),bd=10)
    e_cat.place(relx=.45,rely=.4)
    
    login_btn=Button(frm,command=lambda:addItem_db(),width=8,text="Add",font=('',20,'bold'),bd=10)
    reset_btn=Button(frm,command=lambda:reset_home(),width=8,text="reset",font=('',20,'bold'),bd=10)

    item_label.place(relx=.3,rely=.2)
    item_entry.place(relx=.45,rely=.2)
    
    price_label.place(relx=.3,rely=.3)
    price_entry.place(relx=.45,rely=.3)

    login_btn.place(relx=.35,rely=.5)
    reset_btn.place(relx=.5,rely=.5)

    def addItem_db():
        con=connect("restaurant.sqlite")
        cur=con.cursor()
        it_name=item_entry.get()
        it_price=price_entry.get()
        it_cat=e_cat.get()
        try:
            cur.execute("insert into menucard (Category,Food_item,Rate) values(?,?,?)",(it_cat,it_name,it_price))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Item Added..")
        except:
            messagebox.showwarning("Fail","Try with different Item..")
        
    def reset_home():
        item_entry.delete(0,END)
        price_entry.delete(0,END)
        e_cat.delete(0,END)
        item_entry.focus()

    def back():
        frm.destroy()
        welcome_screen()
    
    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()


def editprice_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    title_lbl=Label(frm,text="Edit Price",font=('',50,'bold','italic'),bg='pink',fg='green')
    title_lbl.place(relx=.35,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    back_btn=Button(frm,command=lambda:back(),width=6,text="back",font=('',20,'bold'),bd=10)
    back_btn.place(x=1,y=60)

    con=connect('restaurant.sqlite')
    cur=con.cursor()
    cur.execute("select distinct(category) from menucard")
    rows=cur.fetchall()
    category=[]
    for row in rows:
        category.append(row[0])

    con.close()

    
    l_cat=Label(frm,text="Select Category",font=('',20,'bold'),bg='pink')
    l_cat.place(relx=.3,rely=.2)
                        
    cb_cat=Combobox(frm,font=('',20,'bold'),values=category)
    cb_cat.place(relx=.45,rely=.2)
    cb_cat.current(0)
    
    
    l_item=Label(frm,text="Select Item",font=('',20,'bold'),bg='pink')
    l_item.place(relx=.3,rely=.3)
    
    categ=cb_cat.get()
    con=connect('restaurant.sqlite')
    cur=con.cursor()
    cur.execute("select * from menucard where category=?",(categ,))
    rows=cur.fetchall()
    fooditems=[]
    for row in rows:
        fooditems.append(row[2])
    con.close()
    
    cb_item=Combobox(frm,font=('',20,'bold'),values=fooditems,state="readonly")
    cb_item.place(relx=.4,rely=.3)
    #cb_item.current(0)
    
    l_rate=Label(frm,text="Set Price",font=('',20,'bold'),bg='pink')
    l_rate.place(relx=.3,rely=.4)
                        
    e_rate=Entry(frm,font=('',20,'bold'),bd=10)
    e_rate.place(relx=.4,rely=.4)

    
    def select_item(event):
        categ=cb_cat.get()
        cb_item.configure(state="normal")
        cb_item.delete(0,END)
        cb_item.configure(state="readonly")
        con=connect('restaurant.sqlite')
        cur=con.cursor()
        cur.execute("select * from menucard where category=?",(categ,))
        rows=cur.fetchall()
        fooditems=[]
        for row in rows:
            fooditems.append(row[2])
        cb_item.configure(values=fooditems)
        con.close()
        
    cb_cat.bind('<<ComboboxSelected>>',select_item)

    update_btn=Button(frm,command=lambda:updatePrice_db(),width=8,text="Update",font=('',20,'bold'),bd=10)
    reset_btn=Button(frm,command=lambda:reset_home(),width=8,text="Reset",font=('',20,'bold'),bd=10)
    
    update_btn.place(relx=.37,rely=.52)
    reset_btn.place(relx=.52,rely=.52)


    def updatePrice_db():
        cat=cb_cat.get()
        item=cb_item.get()
        price=e_rate.get()
        con=connect("restaurant.sqlite")
        cur=con.cursor()
        cur.execute("update menucard set rate=? where food_item=? and category=?",(price,item,cat))
        con.commit()
        con.close()
        messagebox.showinfo("Success","Price updated")
    
    def reset_home():
        cb_cat.delete(0,END)
        cb_item.configure(state="normal")
        cb_item.delete(0,END)
        cb_item.configure(state="readonly")
        e_rate.delete(0,END)
        cb_cat.focus()


    def back():
        frm.destroy()
        welcome_screen()

    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()

def billing_screen():
    frm=Frame(win,bg='pink')
    frm.place(x=0,y=200,relwidth=1,relheight=.9)

    welcome_lbl=Label(frm,text="Welcome,Admin",font=('',20),bg='pink')
    welcome_lbl.place(x=1,y=14)

    l_billing=Label(frm,text="Billing",font=('',50,'bold','italic'),bg='pink',fg='green')
    l_billing.place(relx=.35,y=14)

    logout_btn=Button(frm,command=lambda:logout(),width=8,text="logout",font=('',20,'bold'),bd=10)
    logout_btn.place(relx=.88,y=1)

    back_btn=Button(frm,command=lambda:back(),width=6,text="back",font=('',20,'bold'),bd=10)
    back_btn.place(x=1,y=60)

    con=connect('restaurant.sqlite')
    cur=con.cursor()
    cur.execute("select distinct(category) from menucard")
    rows=cur.fetchall()
    category=[]
    for row in rows:
        category.append(row[0])
    con.close()
    
    l_cat=Label(frm,text="Category",font=('',15,'bold'),bg='pink')
    l_cat.place(relx=.1,rely=.15)
    
    cb_cat=Combobox(frm,font=('',15,'bold'),values=category,state="readonly")
    cb_cat.place(relx=.2,rely=.15)
    cb_cat.current(0)

    l_item=Label(frm,text="Select Item",font=('',15,'bold'),bg='pink')
    l_item.place(relx=.1,rely=.25)
    
    categ=cb_cat.get()
    con=connect('restaurant.sqlite')
    cur=con.cursor()
    cur.execute("select * from menucard where category=?",(categ,))
    rows=cur.fetchall()
    fooditems=[]
    for row in rows:
        fooditems.append(row[2])
    con.close()
    
    cb_item=Combobox(frm,font=('',15,'bold'),values=fooditems,state="readonly")
    cb_item.place(relx=.2,rely=.25)
    cb_item.current(0)

    l_qty=Label(frm,text="Select Qty",font=('',15,'bold'),bg='pink')
    l_qty.place(relx=.1,rely=.35)
    
    cb_qty=Combobox(frm,font=('',15,'bold'),values=[1,2,3,4,5])
    cb_qty.place(relx=.2,rely=.35)
    cb_qty.current(0)
    
    def select_item(event):
        categ=cb_cat.get()
        cb_item.configure(state="normal")
        cb_item.delete(0,END)
        cb_item.configure(state="readonly")
        con=connect('restaurant.sqlite')
        cur=con.cursor()
        cur.execute("select * from menucard where category=?",(categ,))
        rows=cur.fetchall()
        fooditems=[]
        for row in rows:
            fooditems.append(row[2])
        cb_item.configure(values=fooditems)
        con.close()
        
    cb_cat.bind('<<ComboboxSelected>>',select_item)
    
    add_btn=Button(frm,command=lambda:add_item_to_details(),width=8,text="add",font=('',15,'bold'),bd=5)
    add_btn.place(relx=.15,rely=.42)
    
    delete_btn=Button(frm,command=lambda:delete_item_to_details(),width=8,text="delete",font=('',15,'bold'),bd=5)
    delete_btn.place(relx=.25,rely=.42)
    

    date=str(datetime.now())
    Label(frm,text=f"{date}",font=('',13,'bold'),bg='pink',fg='blue').place(relx=.7,rely=0)

    

    billed_items={}
    table=0
    def add_item_to_details():
        nonlocal billed_items,table
        cat=cb_cat.get()
        item=cb_item.get()
        qty=cb_qty.get()
        con=connect('restaurant.sqlite')
        cur=con.cursor()
        cur.execute("select rate from menucard where category=? and food_item=?",(cat,item))
        row=cur.fetchone()
        price=row[0]
        con.close()
        amount=int(qty)*price
        billed_items[item]=[qty,price,int(qty)*price]
        table=Treeview(frm,columns=("Food_item","Qty","Price/Unit","Amount"),show="headings")
        
        table.heading("Food_item",text="Food item")
        table.heading("Qty",text="Qty")
        table.heading("Price/Unit",text="Price/Unit")
        table.heading("Amount",text="Amount")
        table.place(relx=.39,rely=.15,width=800,height=400)
        
        table.column('Food_item',width=250)
        table.column('Qty',width=100)
        
        sb=Scrollbar(table,orient='vertical',command=table.yview)
        sb.place(x=785,y=0,height=400)
        table.configure(yscrollcommand=sb.set)
        
        style = Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),foreground='black')
        style1=Style()
        style1.configure("Treeview", font=('Arial',15,'bold'),foreground='black')
        
        for i in billed_items:
            table.insert(parent='',index="end", values=(i,billed_items[i][0],billed_items[i][1],billed_items[i][2]))
        
        btn_fb=Button(frm,command=final_bill,width=8,text="final bill",font=('',15,'bold'),bd=5)
        btn_fb.place(relx=.85,rely=.70)
        
        tableselection=0
        def sel_item(event):
            global tableselection
            tableselection=table.selection()
            for i in tableselection:
                print(table.item(i)['values'][0])
            
        table.bind('<<TreeviewSelect>>', sel_item)
        
            
    def delete_item_to_details():
        nonlocal billed_items
        print(billed_items)
        try:
            for i in tableselection:
                billed_items.pop(table.item(i)['values'][0])
                table.delete(i)
            print(billed_items)
            #show_billed_items()
        except Exception as var:
            print(var)
            messagebox.showwarning("Fail","Item not found")

    def show_billed_items():
        print(billed_items)
        
        for i in billed_items:
            table.insert(parent='',index="end", values=(i,billed_items[i][0],billed_items[i][1],billed_items[i][2]))
            

    def final_bill():
        amt=0
        for item in billed_items:
            amt1=billed_items[item][-1]
            amt=amt+amt1
        t_amt=amt*1.05
        messagebox.showinfo("Your Bill:",f"Total Bill:{amt}")
        
        l_gst=Label(frm,text=f"Total amount= {amt} \nTotal bill @5%GST= {t_amt}",font=('',15,'bold'),bd=5,bg='pink',fg='black')
        l_gst.place(relx=.65,rely=.70)
        
        l_email=Label(frm,text="Your email ID",font=('',20),bg='pink')
        l_email.place(relx=0.015,rely=.55)
        
        e_email=Entry(frm,font=('',20),bd=10)
        e_email.place(relx=0.15,rely=.55)
        e_email.focus()
        
        l_apass=Label(frm,text="App password",font=('',20),bg='pink')
        l_apass.place(relx=0.01,rely=.65)
        
        e_apass=Entry(frm,font=('',20),bd=10)
        e_apass.place(relx=0.15,rely=.65)
        
        l_cemail=Label(frm,text="Customer mail ID",font=('',20),bg='pink')
        l_cemail.place(relx=0.01,rely=.75)
        
        e_cemail=Entry(frm,font=('',20),bd=10)
        e_cemail.place(relx=0.17,rely=.75)
        
        def sendmail():
            id=e_email.get()
            apass=e_apass.get()
            c_id=e_cemail.get()
            
            connection=gmail.GMail(id,apass)   #'Kand Poha': ['1', 70, 70]
            yourbill="| Food_item\t\t\t|Qty\t|Price/Unit\t|Amount\t\t| \n__________________________________________________________________________"
            
            totalbill=0
            for i in billed_items:
                if len(i)<26:
                    leng=26-len(i)
                    j=""
                    for k in range(0,leng):
                        j=j+" "
                j=i+j
                yourbill=yourbill+f'\n|{j}\t|{billed_items[i][0]}\t|{billed_items[i][1]}\t\t|{billed_items[i][2]}\t\t|'
                totalbill=totalbill+billed_items[i][2]
            print(yourbill)
            print(totalbill)
            try:
                msg=gmail.Message(to=c_id,subject="Customer Bill Payment Receipt",text=f"""Dear Customer, \n\nPlease find your bill, hope you are satisfied with our food quality and services.Please feel free to give us your feedback on the same thread so further we can improve. \n\n {yourbill} \n\nTotal= {totalbill}\nTotal Payable Amount @5%GST= {totalbill*1.05} \n\nThank you & Visit Again""")
                connection.send(msg)
            except:
                messagebox.showerror("Invalid mail id password or No connection","Please check the entered mailID password \nand Internet Connection then Try Again!!")
            else:
                messagebox.showinfo("Success","Mail send to customer ID,\nSuccessfully!!")
        
        btn_mail=Button(frm,command=sendmail,width=12,text="Send Mail",font=('',15,'bold'),bd=10)
        btn_mail.place(relx=.39,rely=.75)
        
    
    def reset_home():
        cb_cat.configure(state="normal")
        cb_item.configure(state="normal")
        cb_cat.delete(0,END)
        cb_qty.delete(0,END)
        cb_item.delete(0,END)
        cb_cat.configure(state="readonly")
        cb_item.configure(state="readonly")
        cb_cat.focus()


    def back():
        frm.destroy()
        welcome_screen()

    def logout():
        option=messagebox.askyesno('confirmation','Do you want to logout?')
        if(option==True):
            frm.destroy()
            home_screen()


home_screen()
win.mainloop()
