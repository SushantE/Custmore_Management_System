from tkinter import *
import time
from subprocess import call
root=Tk()
root.title("Customer Relationship Management(CRM-Portal)")
root.geometry("963x749+540+110")

#======================------Call another page using calling function subprocess-------=================================

def Add_ctmr():
    call(["python", "Add_customer.py"])
def Add_prdtc():
    call(["python", "Add_products.py"])
"""def payment():
    call(["python", "Payment_details.py"])"""


#=======================================--------Main_Frame--------======================================================
Frame_1=Frame(root)
Frame_1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
Frame_1.configure(relief=GROOVE)
Frame_1.configure(borderwidth="15")
Frame_1.configure(relief=GROOVE)
Frame_1.configure(background="#008B8B")	#d9d9d9
Frame_1.configure(highlightbackground="#d9d9d9")
Frame_1.configure(highlightcolor="black")
Frame_1.configure(width=925)
#=======================================------------Frame-2-------======================================================

Frame_2=Frame(root)
Frame_2.place(relx=0.37, rely=0.01, relheight=0.07, relwidth=0.25)
Frame_2.configure(relief=GROOVE)
Frame_2.configure(borderwidth="8")
Frame_2.configure(relief=GROOVE)
Frame_2.configure(background="#d9d9d9")	 #008B8B
Frame_2.configure(highlightbackground="#d9d9d9")
Frame_2.configure(highlightcolor="black")
Frame_2.configure(width=50)
#======================================================================================================================

#=======================================--------Welcome_Message--------=================================================

Message_1=Message(Frame_1,text="Welcome-CRM",font=("bold",25))
Message_1.place(relx=0.35, rely=0.07, relheight=0.07, relwidth=0.30)

Message_1.configure(background="#008B8B") #d9d9d9 #008B8B
Message_1.configure(foreground="white")
Message_1.configure(highlightbackground="#d9d9d9")
Message_1.configure(highlightcolor="black")
Message_1.configure(width=791)
#=======================================--------Time_format--------=====================================================

localtime=time.asctime(time.localtime(time.time()))

set_time=Message(Frame_2,text=localtime,font=("bold",14),bd=5)
set_time.place(relx=0.00, rely=0.00, relheight=0.99, relwidth=0.99)

set_time.configure(background="red") #d9d9d9 #008B8B
set_time.configure(foreground="white")
set_time.configure(highlightbackground="#d9d9d9")
set_time.configure(highlightcolor="black")
set_time.configure(width=791)

#============================---------Add_Customer-Button_1----------===================================================

Button_1=Button(Frame_1,text="1.Add Customer",bd=10)
Button_1.place(relx=0.18, rely=0.17, height=103, width=566)
Button_1.configure(activebackground="#4169E1")
Button_1.configure(activeforeground="White")
Button_1.configure(background="#563BDB") #d9d9d9
#Button_1.configure(disabledforeground="#bfbfbf")
Button_1.configure(font="font14")
Button_1.configure(foreground="white")#000000
Button_1.configure(highlightbackground="#d9d9d9")
Button_1.configure(highlightcolor="black")
Button_1.configure(pady="0")
Button_1.configure(width=566)
Button_1.configure(command=Add_ctmr)


#============================---------Add_Product-Button_2----------===================================================


Button_2 = Button(Frame_1,text="2.Add Product",bd=10)
Button_2.place(relx=0.18, rely=0.33, height=93, width=566)
Button_2.configure(activebackground="#179be8")
Button_2.configure(activeforeground="white")
Button_2.configure(background="#006400") #d9d9d9
Button_2.configure(disabledforeground="#bfbfbf")
Button_2.configure(font="font14")
Button_2.configure(foreground="white")#000000
Button_2.configure(highlightbackground="#d9d9d9")
Button_2.configure(highlightcolor="black")
Button_2.configure(pady="0")
Button_2.configure(width=566)
Button_2.configure(command=Add_prdtc)


#============================---------Pyment_Details-Button_3----------=================================================

Button_3 = Button(Frame_1,text="3.Payment Details",bd=10)
Button_3.place(relx=0.18, rely=0.48, height=93, width=566)
Button_3.configure(activebackground="#FFD700")
Button_3.configure(activeforeground="white")
Button_3.configure(background="#FFA500")	#d9d9d9
Button_3.configure(disabledforeground="#bfbfbf")
Button_3.configure(font="font14")
Button_3.configure(foreground="white")
Button_3.configure(highlightbackground="#d9d9d9")
Button_3.configure(highlightcolor="black")
Button_3.configure(pady="0")
Button_3.configure(width=566)
#Button_3.configure(command=Paymen_deatails)

#============================---------Exit-Button_3----------===========================================================
Button_4 = Button(Frame_1,text='''4.EXIT''',bd=10)
Button_4.place(relx=0.41, rely=0.63, height=70, width=150)
Button_4.configure(activebackground="#F2461B")
Button_4.configure(activeforeground="white")
Button_4.configure(background="#FA8072")
Button_4.configure(disabledforeground="#bfbfbf")
Button_4.configure(font="font14")
Button_4.configure(foreground="white")
Button_4.configure(highlightbackground="#d9d9d9")
Button_4.configure(highlightcolor="black")
Button_4.configure(pady="0")
Button_4.configure(width=566)
Button_4.configure(command=quit)



root.mainloop()