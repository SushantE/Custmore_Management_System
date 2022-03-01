import mysql.connector
from tkinter import messagebox


def customer_insert_record(customer_id,customer_name,customer_address,mobile_number,email,gender):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crm_test"
    )

    """if mydb:
        print("Connection Successful.")
    else:
        print("No Connection.")

    print(customer_id,customer_name,customer_address,mobile_number,email,gender)"""

    mycursor = mydb.cursor()

    sql = "INSERT INTO `customer_details`(`customer_id`, `customer_name`, `address`, `gender`, `email_id`, `mobile_no`)" \
          " VALUES (%s,%s,%s,%s,%s,%s)"
    val = (customer_id, customer_name, customer_address, gender, email, mobile_number)
    mycursor.execute(sql, val)

    mydb.commit()
    x = mycursor.rowcount
    messagebox.showinfo("Record", "records are inserted.{}".format(x))




