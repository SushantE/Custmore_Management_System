from tkinter import*
#from tkinter import ttk, messagebox
from insert_product_db import*
from subprocess import call


root=Tk()
root.title("Customer Relationship Management(CRM-Portal)")
root.geometry("1000x1000")

#================================================Add Product-Frame_0===========================================================
Frame0=Frame(root)
Frame0.place(relx=0.03, rely=0.01, relheight=0.08, relwidth=0.95)
Frame0.configure(relief=GROOVE)
Frame0.configure(borderwidth="7")
Frame0.configure(relief=GROOVE)
Frame0.configure(background="yellow")
Frame0.configure(highlightbackground="#ffffff")
Frame0.configure(highlightcolor="black")

var=StringVar()
msg_1=Label(Frame0, text="-----:- Add Product -:----- ",font=("Times New Roman", 30),fg='blue',bg='yellow',width=41)
msg_1.grid(row=0, column=0, padx=40)
#================================================Frame-1================================================================

Frame1 = Frame(root)
Frame1.place(relx=0.03, rely=0.09, relheight=0.53, relwidth=0.95)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="5")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="#20BD79")
Frame1.configure(highlightbackground="#ffffff")
Frame1.configure(highlightcolor="black")
#Frame1.configure(width=995)
#============================Frame-2(where add,clear and exit button are present )======================================

Frame2 = Frame(Frame1)
Frame2.place(relx=0.31, rely=0.76, relheight=0.18, relwidth=0.34)
Frame2.configure(relief=GROOVE)
Frame2.configure(borderwidth="10")
Frame2.configure(relief=GROOVE)
Frame2.configure(background="#20BD79")#563BDB
Frame2.configure(highlightbackground="#ffffff")
Frame2.configure(highlightcolor="black")
Frame2.configure(width=50)
#========================Frame-3(where product details-{click here} button are present )================================

Frame3 = Frame(root)
Frame3.place(relx=0.03, rely=0.60, relheight=0.20, relwidth=0.95)
Frame3.configure(relief=GROOVE)
Frame3.configure(borderwidth="10")
Frame3.configure(relief=GROOVE)
Frame3.configure(background="#A7A0F4")
Frame3.configure(highlightbackground="#ffffff")
Frame3.configure(highlightcolor="black")
Frame3.configure(width=93)
#------------------------------------------Show Customer Details--------------------------
Lbl_1=Label(Frame3,text='''Show Product Details''',bg='#A7A0F4',font='bold, 20',fg='#3505D2')
Lbl_1.place(relx=0.35, rely=0.04)
#------------------------------------------Click-Button--------------------------

def click():#use call function for calling (Product _details.py windows)
    call(["python", "Product _details.py"])
    #top=Toplevel(root)
    #top.title('Edit Customer Details')
    #top.geometry("1069x742")

sbmitbtn = Button(Frame3, text = "Click Here",command=click,width='10',font='3',bd='10',bg='green',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.44,rely=0.46)
#======================================================-Declar All_Vraiables-========================================================
entry1_var=StringVar()#IntVar()
entry2_var=StringVar()
entry3_var=StringVar()
entry4_var=StringVar()#IntVar()
entry5_var=StringVar()#IntVar()
#==========================================1-Product Id=================================================================
Lbl_1=Label(Frame1, text="Product Id ",font=("Times New Roman", 20),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.20, rely=0.13, height=47)
Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.45, rely=0.13, height=47)
#==========================================1-Product Id(Entry_box)======================================================

Entry_1=Entry(Frame1,textvariable=entry1_var,bd=3,font="font 20",bg="#FDFD96",foreground='black')
Entry_1.place(relx=0.50, rely=0.15, height=34, relwidth=0.20)
#======================================2=Product Name===================================================================
Lbl_1=Label(Frame1, text=" Product Name ",font=("Times New Roman", 20),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.20, rely=0.27, height=47)

Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.45, rely=0.27, height=47)
#======================================2=Product Name(Entry_box)========================================================
Entry_2=Entry(Frame1,textvariable=entry2_var,bd=3,font="font 20",bg="#FDFD96",foreground='black')
Entry_2.place(relx=0.50, rely=0.29, height=34, relwidth=0.20)

#===================================4=Brand=============================================================================
Lbl_1=Label(Frame1, text=" Brand ",font=("Times New Roman", 20),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.20, rely=0.37, height=47)#

Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.45, rely=0.37, height=47)
#===================================4=Brand(Entry_box)==================================================================

Entry_3=Entry(Frame1,textvariable=entry3_var,bd=3,font="font 20",bg="#FDFD96",foreground='black')
Entry_3.place(relx=0.50, rely=0.40, height=34, relwidth=0.20)#
#=======================================5=Quantity======================================================================
Lbl_1=Label(Frame1, text=" Quantity ",font=("Times New Roman", 20),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.20, rely=0.50, height=47)

Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.45, rely=0.50, height=47)
#===================================5=Quantity(Entry_Box)===============================================================

Entry_4=Entry(Frame1,textvariable=entry4_var,bd=3,font="font 20",bg="#FDFD96",foreground='black')
Entry_4.place(relx=0.50, rely=0.52, height=34, relwidth=0.20)

#====================================6=Price / Unit=====================================================================
Lbl_1=Label(Frame1, text=" Price / Unit ",font=("Times New Roman", 20),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.20, rely=0.60, height=47)

Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#20BD79')
Lbl_1.place(relx=0.45, rely=0.60, height=47)
#====================================6=Price / Unit(Entry_box)==========================================================
Entry_5=Entry(Frame1,textvariable=entry5_var,bd=3,font="font 20",bg="#FDFD96",foreground='black')
Entry_5.place(relx=0.50, rely=0.62, height=34, relwidth=0.20)

#=====================================Function===========================================================================


def fun():
    product_id = str(Entry_1.get())
    product_name = str(Entry_2.get())
    brand = str(Entry_3.get())
    quantity = str(Entry_4.get())
    price_unit = str(Entry_5.get())

    product_insert_record(product_id,product_name,brand,quantity,price_unit)
    """messagebox.showinfo("Submit","Are you sure"+ str((Entry_1.get(),Entry_2.get(),Entry_3.get(),Entry_4.get()
         ,Entry_5.get())))"""
#=============================================Add Product-Button========================================================
sbmitbtn = Button(Frame2,command=fun ,text = "Add",width='6',font='5',bd='5',bg='#77B81D',fg='white'
                  ,activebackground = "green", activeforeground = "magenta").place(relx=0.02,rely=0.09)

#=============================================Exit-Button===============================================================
sbmitbtn = Button(Frame2,command=quit ,text = "Exit",width='6',font='5',bd='5',bg='#CD237A',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.68,rely=0.09)
#=============================================Clearing entry box details================================================
def clearFunc():
    entry1_var.set("")#textvariable=entry1---these clear entry box
    entry2_var.set("")#textvariable=entry2
    entry3_var.set("")#textvariable=entry3
    entry4_var.set("")
    entry5_var.set("")#textvariable=entry5
#=============================================Clear_Button==============================================================
clear_btn = Button(Frame2, text = "Clear",command=clearFunc,width='7',font='5',bd='5',bg='red',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.33,rely=0.05)

root.mainloop()





"""trd=Label(Frame1, text='Product Id',font="5",fg='red',bg='white')
trd.place(relx=0.12, rely=0.03, height=47)
trd=Label(Frame1, text=':',font="5",fg='red',bg='white')
trd.place(relx=0.24, rely=0.03, height=47)
c=StringVar()
list1 = [' 444076',' 444077',' 444078',' 444079',' 444080']

droplist=OptionMenu(Frame1,c, *list1)
droplist.config(width=25,font='italic',fg='green')
c.set('Select')
droplist.place(relx=0.25, rely=0.03, height=47)"""

