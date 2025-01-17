from tkinter import *
from tkinter import ttk,messagebox
from csv import *
def login():
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    l1=Label(f,text="Username",font=("Arial",15),bg="white")
    l1.place(x=50,y=100)
    l2=Label(f,text="Password",font=("Arial",15),bg="white")
    l2.place(x=50,y=140)
    e1=Entry(f,font=("Arial",15),bg="white")
    e1.place(x=150,y=100)
    e2=Entry(f,font=("Arial",15),bg="white",show="*")
    e2.place(x=150,y=140)
    b1=Button(root,text="Login",font=("Arial",15),bg="white",command=lambda:check2(e1,e2))
    b1.place(x=160,y=200)
def signup():
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    l1=Label(f,text="Username",font=("Arial",15),bg="white")
    l1.place(x=50,y=100)
    l2=Label(f,text="Password",font=("Arial",15),bg="white")
    l2.place(x=50,y=140)
    l3=Label(f,text="Confirm Password",font=("Arial",15),bg="white")
    l3.place(x=18,y=180)
    e1=Entry(f,font=("Arial",15),bg="white")
    e1.place(x=150,y=100)
    e2=Entry(f,font=("Arial",15),bg="white",show="*")
    e2.place(x=150,y=140)
    e3=Entry(f,font=("Arial",15),bg="white",show="*")
    e3.place(x=190,y=180)
    b1=Button(root,text="Sign-up",font=("Arial",15),bg="white",command=lambda:check(e1,e2,e3))
    b1.place(x=180,y=230)
def check(e1,e2,e3):
    u1=e1.get()
    p1=e2.get()
    p2=e3.get()
    if p1==p2:
        save(u1,p1)
    else:
        messagebox.showinfo('',"Confirm Password not same as Password")
def save(u1,p1):
    with open("data.csv",'a+',newline='') as f:
        w=writer(f)
        l=[u1,p1]
        w.writerow(l)
    page1()
def check2(e1,e2):
    flag=False
    user=e1.get()
    pas=e2.get()
    with open("data.csv",'r') as f:
        r=reader(f)
        for i in r:
            if i[0]==user and i[1]==pas:
               page1()
               flag=False
               break
            else:
                flag=True
        if (flag):
            messagebox.showinfo('',"Incorrect Details")
def select(tree,l):
    selecteditem = tree.selection()
    item=tree.item(selecteditem)['values'][0]
    l.insert(0,item)

def del1(l):
    for item in l.curselection():
        l.delete(item)
def veg():
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    l=Label(f,text="Available Items",font=("Arial",10),bg="white")
    l.place(x=30,y=30)
    l1=Label(f,text="Selected Items",font=("Arial",10),bg="white")
    l1.place(x=600,y=30)
    tree = ttk.Treeview(f, column=("c1", "c2", "c3"),show='headings', height=7)
    tree.place(x=30,y=50)
    l= Listbox(f,font=("Arial",10))
    l.place(x=600,y=48)
    b1=Button(f,text="Select Item",font=("Arial",10),bg="white",command=lambda :select(tree,l))
    b1.place(x=30,y=230)
    b2=Button(f,text="Remove Item",font=("Arial",10),bg="white",command=lambda :del1(l))
    b2.place(x=600,y=220)
    b3=Button(f,text="Confirm",font=("Arial",15),bg="white",command=lambda :confirm(l,"veg"))
    b3.place(x=300,y=300)
    tree.column("# 1", anchor="w")
    tree.heading("# 1", text="Item")
    tree.column("# 2", anchor="w")
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor="w")
    tree.heading("# 3", text="Persons")
    with open("veg.csv",'r') as f1:
        r=reader(f1)
        print(r)
       
        for i in r:
            tree.insert('', 'end', text="1", values=i)
    bh=Button(f,text="Home",font=("Arial",7),bg="white",command=page1)
    bh.place(x=10,y=10)
    root.mainloop()
def confirm(l,typ):
    items=l.get(0,END)
    req="Reciever"
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    l1=Label(f,text="Name",font=("Arial",15),bg="white")
    l1.place(x=50,y=100)
    l2=Label(f,text="Address",font=("Arial",15),bg="white")
    l2.place(x=50,y=140)
    l3=Label(f,text="Phone-Number",font=("Arial",15),bg="white")
    l3.place(x=30,y=180)
    e1=Entry(f,font=("Arial",15),bg="white")
    e1.place(x=150,y=100)
    e2=Entry(f,font=("Arial",15),bg="white")
    e2.place(x=150,y=140)
    e3=Entry(f,font=("Arial",15),bg="white")
    e3.place(x=180,y=180)
    b1=Button(root,text="Confirm",font=("Arial",15),bg="white",command=lambda:saveinout(e1,e2,e3,items,req,typ))
    b1.place(x=160,y=270)
    bh=Button(f,text="Home",font=("Arial",7),bg="white",command=page1)
    bh.place(x=10,y=10)
def saveinout(e1,e2,e3,items,req,n):
    l=[e1.get(),e2.get(),e3.get(),items,req,n]
    with open("inout.csv",'a+',newline='') as f:
        w=writer(f)
        w.writerow(l)
    if req=="Reciever":
        messagebox.showinfo('',"Order Confirmed !!")
        page1()
    if req=='Sender':
        messagebox.showinfo('',"Thank You For Donating !!")
        page1()
def saveitem(e1,e2,e3,e4,e5,e6,n):
    l=[e1.get(),e2.get(),e3.get()]
    file=n.get()+".csv"
    with open(file,'a+',newline='') as f:
        w=writer(f)
        w.writerow(l)
    saveinout(e4,e5,e6,e1.get(),'Sender',n.get())
def additem():
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    l1=Label(f,text="Item Name",font=("Arial",15),bg="white")
    l1.place(x=50,y=60)
    l2=Label(f,text="QTY",font=("Arial",15),bg="white")
    l2.place(x=50,y=100)
    l3=Label(f,text="Persons",font=("Arial",15),bg="white")
    l3.place(x=50,y=140)
    l4=Label(f,text="Persons-Name",font=("Arial",15),bg="white")
    l4.place(x=30,y=180)
    l5=Label(f,text="Address",font=("Arial",15),bg="white")
    l5.place(x=50,y=220)
    l6=Label(f,text="Phone-Number",font=("Arial",15),bg="white")
    l6.place(x=30,y=260)
    l7=Label(f,text="Item Type",font=("Arial",15),bg="white")
    l7.place(x=30,y=300)
    e1=Entry(f,font=("Arial",15),bg="white")
    e1.place(x=150,y=60)
    e2=Entry(f,font=("Arial",15),bg="white")
    e2.place(x=150,y=100)
    e3=Entry(f,font=("Arial",15),bg="white")
    e3.place(x=150,y=140)
    e4=Entry(f,font=("Arial",15),bg="white")
    e4.place(x=180,y=180)
    e5=Entry(f,font=("Arial",15),bg="white")
    e5.place(x=150,y=220)
    e6=Entry(f,font=("Arial",15),bg="white")
    e6.place(x=180,y=260)
    n = StringVar()
    c= ttk.Combobox(f, width = 10, textvariable = n)
    c['values']=['veg','nonveg']
    c.place(x=180,y=300)
    b1=Button(root,text="ADD",font=("Arial",15),bg="white",command=lambda:saveitem(e1,e2,e3,e4,e5,e6,n))
    b1.place(x=160,y=350)
    bh=Button(f,text="Home",font=("Arial",7),bg="white",command=page1)
    bh.place(x=10,y=10)
def nonveg():
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    l=Label(f,text="Available Items",font=("Arial",10),bg="white")
    l.place(x=30,y=30)
    l1=Label(f,text="Selected Items",font=("Arial",10),bg="white")
    l1.place(x=600,y=30)
    tree = ttk.Treeview(f, column=("c1", "c2", "c3"),show='headings', height=7)
    tree.place(x=30,y=50)
    l= Listbox(f,font=("Arial",10))
    l.place(x=600,y=48)
    b1=Button(f,text="Select Item",font=("Arial",10),bg="white",command=lambda :select(tree,l))
    b1.place(x=30,y=230)
    b2=Button(f,text="Remove Item",font=("Arial",10),bg="white",command=lambda :del1(l))
    b2.place(x=600,y=220)
    b3=Button(f,text="Confirm",font=("Arial",15),bg="white",command=lambda :confirm(l,"nonveg"))
    b3.place(x=300,y=300)
    tree.column("# 1", anchor="w")
    tree.heading("# 1", text="Item")
    tree.column("# 2", anchor="w")
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor="w")
    tree.heading("# 3", text="Persons")
    with open("nonveg.csv",'r') as f1:
        r=reader(f1)
        print(r)
       
        for i in r:
            tree.insert('', 'end', text="1", values=i)
    bh=Button(f,text="Home",font=("Arial",7),bg="white",command=page1)
    bh.place(x=10,y=10)
    root.mainloop()
   
def page1():
    f=Frame(root,bg="white")
    f.place(x=0,y=0,relwidth=2,relheight=2)
    b1=Button(root,text="VEG",font=("Arial",15),bg="white",command=veg)
    b1.place(x=300,y=100)
    b2=Button(root,text="Non-VEG",font=("Arial",15),bg="white",command=nonveg)
    b2.place(x=300,y=160)
    b3=Button(root,text="Add Item",font=("Arial",15),bg="white",command=additem)
    b3.place(x=300,y=220)   
    root.mainloop()
root=Tk()
root.config(bg="white")
root.geometry("800x400")
root.title("DonaSave")
b1=Button(root,text="Login",font=("Arial",20),bg="white",command=login)
b1.place(x=300,y=100)
b2=Button(root,text="Sign up",font=("Arial",20),bg="white",command=signup)
b2.place(x=300,y=200)
root.mainloop()
