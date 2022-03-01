from tkinter import *
#import tkinter as tk
from tkinter import ttk

root=Tk()
root.title("CRM-Portal(Customer Relationship Management Portal")
root.geometry("1069x742")

#-----------------------------------====Customer Details-Frame_0 Title====----------------------------------------------
Frame0=Frame(root)
Frame0.place(relx=0.03, rely=0.01, relheight=0.09, relwidth=0.93)
Frame0.configure(relief=GROOVE)
Frame0.configure(borderwidth="7")
Frame0.configure(relief=GROOVE)
Frame0.configure(background="yellow")
Frame0.configure(highlightbackground="#ffffff")
Frame0.configure(highlightcolor="black")

var=StringVar()
msg_1=Label(Frame0, text="-----:- Customer Details -:----- ",font=("Times New Roman", 30),fg='blue',bg='yellow',width=41)
msg_1.grid(row=0, column=0, padx=40)

#===================================-----Frame_1-----===================================================================
Frame1 = Frame(root)
Frame1.place(relx=0.03, rely=0.10, relheight=0.85, relwidth=0.93)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="15")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="#8023BC")
Frame1.configure(highlightbackground="#ffffff")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=995)



#===============================-----Search By-Customer-----============================================================

# Creating tkinter window
Lbl_1=Label(Frame1, text="Search By ",font=("Times New Roman", 20),fg='white',bg='#8023BC')
#Lbl_1.place(relx=0.20, rely=0.13, height=47)
Lbl_1.grid(row=0, column=0, padx=20,sticky="w")
Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#8023BC')
Lbl_1.grid(row=0, column=1, padx=1,sticky="w")
#Lbl_1.place(relx=0.48, rely=0.13, height=47)

#================================----Combo_Box----======================================================================

n = IntVar()
monthchoosen = ttk.Combobox(Frame1,width=15,font=("times new roman", 13, "bold"),state="readonly")
monthchoosen['values'] = ("Customer Id",'Customer Name')
monthchoosen.grid(row=0,column=1,padx=20,pady=10)
#monthchoosen.place(relx=0.50, rely=0.13, height=47)
# Shows Customer Id as a default value
#monthchoosen.current(1)

#-===============================---Entry---============================================================================
txt_Search=Entry(Frame1,font=("times new roman", 15, "bold"),width=20,bd=10,relief=GROOVE)
txt_Search.grid(row=0,column=2,pady=10,padx=20)

#===========================---Button----===============================================================================
Search_btn=Button(Frame1,text="Search",width=10,pady=5,bd=5).grid(row=0,column=3,padx=10,pady=10)
Show_all_btn=Button(Frame1,text="Show All",width=10,pady=5,bd=5).grid(row=0,column=4,padx=10,pady=10)

#===============================----Table_Frame-2(Where all customer data are store)----================================
Table_Frame=Frame(Frame1,bd=9,relief=RIDGE,bg="#ADFF2F")
Table_Frame.place(x=7,y=70,width=950,height=470)

#=====================================----Scrollbar------===============================================================
scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

#=====================================----TreeView----==================================================================
customer_table=ttk.Treeview(Table_Frame,column=("customer_id", "customer_name", "address", "gender","email_id",
                                                "mobile_no" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=customer_table.xview)
scroll_y.config(command=customer_table.yview)
customer_table.heading("customer_id",text="Customer_Id")
customer_table.heading("customer_name",text="Customer_Name")
customer_table.heading("address",text=" Address")
customer_table.heading("gender",text=" Gender")
customer_table.heading("email_id",text=" E-mail_Id")
customer_table.heading("mobile_no",text="Mobile_Number")

customer_table['show']='headings'
customer_table.column("customer_id",width=100)
customer_table.column("customer_name",width=100)
customer_table.column("address",width=100)
customer_table.column("gender",width=100)
customer_table.column("email_id",width=100)
customer_table.column("mobile_no",width=100)

customer_table.pack(fill=BOTH,expand=1)
#=======================================================================================================================


#===================================----Exit Button----=================================================================
exitbtn = Button(root,command=quit ,text = "Exit",width='8',height='1',font='5',bd='5',bg='red',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.44,rely=0.86)

root.mainloop()
