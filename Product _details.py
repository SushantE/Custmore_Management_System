from tkinter import *
#import tkinter as tk
from tkinter import ttk

root=Tk()
root.title("CRM-Portal(Customer Relationship Management Portal")
root.geometry("1069x742")

#-----------------------------------Product Details Frame with Title----------------------------------------------------
Frame0=Frame(root)
Frame0.place(relx=0.03, rely=0.01, relheight=0.09, relwidth=0.93)
Frame0.configure(relief=GROOVE)
Frame0.configure(borderwidth="7")
Frame0.configure(relief=GROOVE)
Frame0.configure(background="yellow")
Frame0.configure(highlightbackground="#ffffff")
Frame0.configure(highlightcolor="black")

var=StringVar()
msg_1=Label(Frame0, text="--:Product Details:-- ",font=("Times New Roman", 30),fg='blue',bg='yellow',width=41)
msg_1.grid(row=0, column=0, padx=40)


#====================================Frame-1============================================================================

Frame1 = Frame(root)
Frame1.place(relx=0.03, rely=0.10, relheight=0.86, relwidth=0.93)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="15")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="#1D02D8")
Frame1.configure(highlightbackground="#ffffff")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=995)
#====================================Heading title(Search-By)===========================================================
# Creating tkinter window
Lbl_1=Label(Frame1, text="Search By ",font=("Times New Roman", 20),fg='white',bg='#1D02D8')
#Lbl_1.place(relx=0.20, rely=0.13, height=47)
Lbl_1.grid(row=0, column=0, padx=20,sticky="w")
Lbl_1=Label(Frame1, text=":",font=("bold", 25),fg='white',bg='#1D02D8')
Lbl_1.grid(row=0, column=1, padx=1,sticky="w")
#Lbl_1.place(relx=0.48, rely=0.13, height=47)

n=IntVar()
monthchoosen = ttk.Combobox(Frame1,width=15,font=("times new roman", 13, "bold"),state="readonly")
monthchoosen['values'] = ("Product Id",'Product Name')
monthchoosen.grid(row=0,column=1,padx=20,pady=10)
#monthchoosen.place(relx=0.50, rely=0.13, height=47)
# Shows Customer Id as a default value
#monthchoosen.current(1)
#-===============================--Entry--==============================================================================
txt_Search=Entry(Frame1,font=("times new roman", 15, "bold"),width=20,bd=10,relief=GROOVE)
txt_Search.grid(row=0,column=2,pady=10,padx=20)
#==============================Search and Show all Button===============================================================
Search_btn=Button(Frame1,text="Search",width=10,pady=5,bd=5).grid(row=0,column=3,padx=10,pady=10)
Search_btn=Button(Frame1,text="Show All",width=10,pady=5,bd=5).grid(row=0,column=4,padx=10,pady=10)

#=============================================Table Frame-2(Treeview)===================================================
Table_Frame=Frame(Frame1, bd=9, relief=RIDGE, bg="#5EF5F1")
Table_Frame.place(x=8,y=70,width=950,height=470)
#=====================================----Scrollbar------===============================================================

scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
#=====================================----TreeView----==================================================================
product_table=ttk.Treeview(Table_Frame,column=("id","product_id", "product_name","brand", "quantity", "price_unit" ),
                           xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=product_table.xview)
scroll_y.config(command=product_table.yview)
product_table.heading("id",text="Id")
product_table.heading("product_id",text="Product_Id")
product_table.heading("product_name",text=" Product_Name")
product_table.heading("brand",text="Brand")
product_table.heading("quantity",text="Quantity")
product_table.heading("price_unit",text="Price/Unit")

product_table['show']='headings'
product_table.column("id",width=50)
product_table.column("product_id",width=50)
product_table.column("brand",width=50)
product_table.column("quantity",width=50)
product_table.column("price_unit",width=50)

product_table.pack(fill=BOTH,expand=1)

#=======================================Show_details- Button============================================================
"""sbmitbtn = Button(Frame1, text = "Show Details",width='10',height='1',font='5',bd='5',bg='green',fg='white',
activebackground = "red", activeforeground = "magenta").place(relx=0.38,rely=0.40)"""
#=======================================Exit Button=====================================================================
exit_btn = Button(root,command=quit ,text = "Exit",width='10',height='1',font='5',bd='5',bg='red',fg='white',
                  activebackground = "green", activeforeground = "magenta").place(relx=0.44,rely=0.86)

root.mainloop()



#=======================================================================================================================
