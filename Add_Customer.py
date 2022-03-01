from tkinter import *
from tkinter import ttk
from subprocess import call
#from tkinter import messagebox
#import radio as radio
from insert_customer_db import *
#from Customer_details_db import *
root=Tk()
root.title("CRM-Portal(Customer Relationship Management Portal)")
root.geometry("1069x742")

#---------------------------------====-Add Customer Details-Frame_0-Title-====------------------------------------------
Frame0=Frame(root)
Frame0.place(relx=0.03, rely=0.01, relheight=0.09, relwidth=0.93)
Frame0.configure(relief=GROOVE)
Frame0.configure(borderwidth="7")
Frame0.configure(relief=GROOVE)
Frame0.configure(background="yellow")
Frame0.configure(highlightbackground="#ffffff")
Frame0.configure(highlightcolor="black")

var=StringVar()
msg_1=Label(Frame0, text="-----:- Add Customer Details -:----- ",font=("Times New Roman", 30),fg='blue',bg='yellow',width=41)
msg_1.grid(row=0, column=0, padx=40)


#================================================----Frame_1----========================================================

Frame1 = Frame(root)
Frame1.place(relx=0.03, rely=0.10, relheight=0.53, relwidth=0.93)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="10")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="#563BDB")
Frame1.configure(highlightbackground="#ffffff")
Frame1.configure(highlightcolor="black")
#Frame1.configure(width=995)
#============================----Frame-2(where add,clear,edit and exit button are present )----=========================

Frame2 = Frame(Frame1)
Frame2.place(relx=0.25, rely=0.76, relheight=0.18, relwidth=0.55)
Frame2.configure(relief=GROOVE)
Frame2.configure(borderwidth="6")
Frame2.configure(relief=GROOVE)
Frame2.configure(background="#563BDB")#563BDB
Frame2.configure(highlightbackground="#ffffff")
Frame2.configure(highlightcolor="black")
Frame2.configure(width=50)
#========================---Frame-3(where customer details-{click here} button are present )---=========================


Frame3 = Frame(root)
Frame3.place(relx=0.03, rely=0.63, relheight=0.20, relwidth=0.93)
Frame3.configure(relief=GROOVE)
Frame3.configure(borderwidth="10")
Frame3.configure(relief=GROOVE)
Frame3.configure(background="#abe1f7")
Frame3.configure(highlightbackground="#ffffff")
Frame3.configure(highlightcolor="black")
Frame3.configure(width=93)

             #-----------------------------------------=-Show Customer Details-=-------------------------
Lbl_1=Label(Frame3,text='''Show Customer Details''',bg='#abe1f7',font='bold, 20',fg='#3505D2')
Lbl_1.place(relx=0.35, rely=0.04)
             #---------------------------------------------=-Click-Button-=------------------------------

def click():#use call function for calling (Customer _details.py windows)
    call(["python", "Customer_details.py"])
    #top=Toplevel(root)
    #top.title('Edit Customer Details')
    #top.geometry("1069x742")

sbmitbtn = Button(Frame3, text = "Click Here",command=click,width='10',font='3',bd='10',bg='green',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.44,rely=0.46)
#===============================================----All_Vraiables----===================================================
entry1=StringVar()#IntVar()
entry2=StringVar()
entry3=StringVar()
combo4=StringVar()#IntVar()
entry5=StringVar()#IntVar()
entry6=StringVar()


#-================================================----Customer_Id----===================================================
Lbl_1=Label(Frame1,text='''Customer Id''',bg='#563BDB',font='bold, 15',width=20,highlightcolor="black",fg='white')
Lbl_1.place(relx=0.0, rely=0.03, height=47)

Lbl_2=Label(Frame1, text=''':''', bg='#563BDB', font='bold, 15', borderwidth="2",highlightcolor="black",fg='white')
Lbl_2.place(relx=0.25, rely=0.03, height=47,width=26)
#-================================================----Customer_Id(Entry_box)----========================================

Entry_1=Entry(Frame1,bd=3,font="font 20",bg="#FDFD96",foreground='green',textvariable=entry1)
Entry_1.place(relx=0.30, rely=0.06, height=34, relwidth=0.43)
#=================================================----2-Customer Name----===============================================
Lbl_1=Label(Frame1,text='''Customer Name''',bg='#563BDB',font='bold, 15',width=20,highlightcolor="black",fg='white')
Lbl_1.place(relx=0.02, rely=0.16, height=47)

Lbl_2=Label(Frame1, text=''':''', bg='#563BDB', font='bold, 15', borderwidth="2",highlightcolor="black",fg='white')
Lbl_2.place(relx=0.25, rely=0.16, height=47,width=26)
#=================================================----2-Customer Name(Entry_box)----====================================

Entry_2=Entry(Frame1,bd=3,font="font 20",bg="#FDFD96",foreground='green',textvariable=entry2)
Entry_2.place(relx=0.30, rely=0.18, height=34, relwidth=0.43)
#=================================================----3-Customer Address----============================================

Lbl_1=Label(Frame1,text='''Customer Address''',bg='#563BDB',font='bold, 15',width=20,highlightcolor="black",fg='white')
Lbl_1.place(relx=0.03, rely=0.28, height=47)

Lbl_2=Label(Frame1, text=''':''', bg='#563BDB', font='bold, 15', borderwidth="2",highlightcolor="black",fg='white')
Lbl_2.place(relx=0.25, rely=0.28, height=47,width=26)
#=================================================----3-Customer Address(Entry_box)----=================================

Entry_3=Entry(Frame1,bd=3,font="font 20",bg="#FDFD96",foreground='green',textvariable=entry3)
Entry_3.place(relx=0.30, rely=0.30, height=34, relwidth=0.43)

#==================================================--------4=Gender-------==============================================

Lbl_1=Label(Frame1,text='''Gender        ''',bg='#563BDB',font='bold, 15',width=20,highlightcolor="black",fg='white')
Lbl_1.place(relx=0.01, rely=0.39, height=47)

Lbl_2=Label(Frame1, text=''':''', bg='#563BDB', font='bold, 15', borderwidth="2",highlightcolor="black",fg='white')
Lbl_2.place(relx=0.25, rely=0.39, height=47,width=26)
#==================================================--------4=Gender(Combo_box)-------===================================

combo_gender=ttk.Combobox(Frame1,font=("times new roman", 14, "bold"),state='readonly',width=7,textvariable=combo4)
combo_gender['values']=("Male","Female")
combo_gender.place(relx=0.30, rely=0.42)


"""Radio_var=IntVar()
R1 = Radiobutton(Frame1, text="Male", variable=radio, value=1,font="5",fg='teal',activeforeground='magenta',bg='white')
R1.place(relx=0.30, rely=0.46)
#R1.grid(row=0,column=0)
R2 = Radiobutton(Frame1, text="Female", variable=radio,value=2,font="5",fg='teal',activeforeground='magenta',bg='white')
R2.place(relx=0.40, rely=0.46)
#R2.grid(row=1,column=0)"""
#==================================================----5=Mobile Number----==============================================

Lbl_1=Label(Frame1,text='''Mobile Number''',bg='#563BDB',font='bold, 15',width=20,highlightcolor="black",fg='white')
Lbl_1.place(relx=0.02, rely=0.51, height=47)

Lbl_4=Label(Frame1, text=''':''', bg='#563BDB', font='bold, 15', borderwidth="2",highlightcolor="black",fg='white')
Lbl_4.place(relx=0.25, rely=0.51, height=47,width=26)
#==================================================----5=Mobile Number(Entry_box)----===================================

Entry_4=Entry(Frame1,bd=3,font="font 20",bg="#FDFD96",foreground='green',textvariable=entry5)
Entry_4.place(relx=0.30, rely=0.53, height=34, relwidth=0.22)

#=============================================----6=Email-Id----========================================================

Lbl_1=Label(Frame1,text='''E-mail     ''',bg='#563BDB',font='bold, 15',highlightcolor="black",fg='white')
Lbl_1.place(relx=0.06, rely=0.63, height=47)

Lbl_2=Label(Frame1, text=''':''', bg='#563BDB', font='bold, 15',fg='white')
Lbl_2.place(relx=0.25, rely=0.63, height=47,width=26)
#========================================----6=Email-Id(Entry_box)----==================================================

Entry_5=Entry(Frame1,bd=3,font="font 20",bg="#FDFD96",foreground='green',textvariable=entry6)
Entry_5.place(relx=0.30, rely=0.65, height=34, relwidth=0.43)

#==============================------(Function )--------================================================================
def customer_form():
    customer_id=str(Entry_1.get())
    customer_name = str(Entry_2.get())
    customer_address = str(Entry_3.get())
    gender = str(combo_gender.get())
    mobile_number = str(Entry_4.get())
    email = str(Entry_5.get())
    #gender = None
    customer_insert_record(customer_id,customer_name,customer_address,mobile_number,email,gender)


    """messagebox.showinfo("submit?", "You selected the option " + 
                        str((Entry_1.get(),Entry_2.get(),Entry_3.get(),Entry_4.get(),Entry_5.get())))"""

#==============================--------Add-Buttom--------==============================================================

sbmitbtn = Button(Frame2, text = "Add",command=customer_form,width='10',height='1',font='5',bd='5',bg='#77B81D',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.01,rely=0.09)

#=================================================----calling function----===================================================
#from tkinter import*

def edit():#use call function for calling (update_customer.py windows)
    call(["python", "update_customer.py"])
    #top=Toplevel(root)
    #top.title('Edit Customer Details')
    #top.geometry("1069x742")
#=================================================----Edit-Button----===================================================

edit_btn = Button(Frame2, text = "Edit",command=edit,width='10',height='1',font='3',bd='5',bg='#33FF99',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.29,rely=0.09)
#==============================================-----using function Clear-text-in-Enty-box -----=========================
def clearFunc():
    entry1.set("")#textvariable=entry1---these clear entry box
    entry2.set("")#textvariable=entry2
    entry3.set("")#textvariable=entry3
    combo4.set("")
    entry5.set("")#textvariable=entry5
    entry6.set("")#textvariable=entry6
#=============================================Clear_Button==============================================================

clear_btn = Button(Frame2, text = "Clear",command=clearFunc,width='10',height='1',font='5',bd='5',bg='red',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.56,rely=0.09)
#==========================================================----Exit-Button---===========================================
"""def quit():
    messagebox.askyesnocancel("Add Customer","Do you want to exit the sysyem?")"""

exit_btn = Button(Frame2,command=quit ,text = "Exit",width='5',height='1',font='5',bd='5',bg='#CD237A',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.84,rely=0.09)


root.mainloop()