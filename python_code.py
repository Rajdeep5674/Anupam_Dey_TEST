import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@jdeep123",
    database="June_python_project")
cur_obj=conn_obj.cursor()

#Define function data_entry_sql
def data_entry_sql(cust_name,cust_address,cust_ph_no):

    # Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO cust_table (cust_name,cust_address,cust_ph_no) VALUES (%s, %s, %s)"
    data = (cust_name,cust_address,cust_ph_no)

    try:
        cur_obj.execute(sql, data)
        print("Customer details sucessfully inserted.")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

#Define function data_retrieve
def data_retrieve(cust_ph_no):
    # Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    query = f"select * from cust_table WHERE cust_ph_no={cust_ph_no}"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Print or process the retrieved data using list unpacking
    if result:
        print(result)
        return 1
    else:
        print("Customer details not present. Please collect details from customer.")
        return 0

def data_retrieve_from_inventory(product_id):
    query = f"select * from inventory_table WHERE p_id={product_id}"
    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Print or process the retrieved data using list unpacking
    if result:
        return result
    else:
        print("product not found")
        return 0

cust_ph_no=input("please enter your phone number - ")
result_from_retrive_function=data_retrieve(cust_ph_no)
if result_from_retrive_function==0:
    cust_name=input("please enter your full name- ")
    cust_address=input("please enter your address- ")
    data_entry_sql(cust_name,cust_address,cust_ph_no)

def operation():
    product_id=int(input("please enter the product id- "))
    product_quantity=float(input("please enter the product quantity- "))
    product_details_from_db=data_retrieve_from_inventory(product_id)
    print(product_details_from_db[2])
    print("amount to be paid- ",float(product_details_from_db[2])*product_quantity)
operation()
conn_obj.close()