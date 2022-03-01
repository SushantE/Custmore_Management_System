import mysql.connector
from tkinter import messagebox
def product_insert_record(product_id, product_name, brand, quantity,price_unit):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="crm_test"
    )

    if mydb:
        print("Connection Successful.")
    else:
        print("No Connection.")
    #print(product_id,product_name,brand,quantity,price_unit)


    mycursor = mydb.cursor()

    sql = "INSERT INTO `product_details`(`product_id`, `product_name`, `brand`, `quantity`, `price_unit`) " \
          "VALUES ( %s,%s,%s,%s,%s)"
    val = (product_id, product_name, brand, quantity, price_unit)

    mycursor.execute(sql, val)

    mydb.commit()
    x = mycursor.rowcount
    messagebox.showinfo("Product Record", "records are inserted.{}".format(x))
