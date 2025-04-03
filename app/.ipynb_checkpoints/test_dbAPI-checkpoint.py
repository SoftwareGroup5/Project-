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


if __name__ == "__main__":
    
    #create database with name from above 
    dbAPI.create(myDB)

    #populate different tables in myDB with data
    dbAPI.fill_orders(myDB)

    #prints out entries in each table so we can visually confirm they're populating
    test_orders(myDB)