import mysql.connector
#import pymysql

from tkinter import messagebox
def customer_update_record(customer_name, address, gender, email_id, mobile_no, customer_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="crm_test"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE `customer_details` SET `customer_name`=%s,`address`=%s,`gender`=%s,`email_id`=%s,`mobile_no`=%s " \
          "WHERE `customer_id`=%s"
    val = ( customer_name, address, gender, email_id, mobile_no, customer_id)

    mycursor.execute(sql, val)

    mydb.commit()
    x = mycursor.rowcount
    messagebox.showinfo("Product Record", "records are updated.{}".format(x))

    #print(mycursor.rowcount, "record updated.")
