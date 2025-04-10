#purpose: test functions in dbAPI.py, calls create + fill and then prints out the tables that should be populated so we can visually confirm 
#usage: 
    # python test_dbAPI.py
    #must be in same repo as dbAPI.py
    #change myDB variable to adjust name of created database


import dbAPI #import the dpAPI file with the functions we want to test
import sqlite3

#name of created database. change to whatever 
myDB = "DB"

def test_orders(DB):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    data = c.execute("SELECT * FROM orders")
    print("Table: orders")
    for row in data:
        print(row)
    return 

def test_customers(DB):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    data = c.execute("SELECT * FROM customer_table")
    print("Table: customer_table")
    for row in data:
        print(row)
    return

def test_get_customer_by_id(DB, customer_id):
    customer = dbAPI.get_customer_by_id(DB, customer_id)
    print(f"Customer with id {customer_id}: {customer}")

def test_get_cart_for_customer(DB, customer_id):
    print("Testing cart retrieval for customer:", customer_id)
    print(dbAPI.get_cart_for_customer(DB, customer_id))


if __name__ == "__main__":
    #checks if db exist and clears if so"
    print(dbAPI.delete_db(myDB))
    #create database with name from above 
    dbAPI.create(myDB)
    
    #fills auth_table
    print(dbAPI.fill_auth(myDB))
    
    #test authorize
    print(dbAPI.authorize(myDB, 'admin', 'root'))
    
    #fills order_history
    print(dbAPI.fill_order_history(myDB))

    #fill customer_table
    print(dbAPI.fill_customers(myDB))
    
    #fill product
    dbAPI.fill_products(myDB)

    #print out entries in customer_table to confirm
    test_customers(myDB)
    
    #fill orders table 
    dbAPI.fill_orders(myDB)

    #prints out entries in each table so we can visually confirm they're populating
    test_orders(myDB)


    #prints the retrieved customer record for the specified customer ID
    test_get_customer_by_id(myDB, 101)
    
    test_get_cart_for_customer(myDB, 345)
