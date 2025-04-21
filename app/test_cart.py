#written by: Nicole Cosmany
#date: 4/152025
#purpose: test cart functions 

import unittest
import dbAPI
import sqlite3
import os

class Test_CartFunctions(unittest.TestCase):
    myDB = "myDB"
    
    #create DB and populate test data
    def setUp(self):
        dbAPI.create(self.myDB)
        dbAPI.fill_customers(self.myDB)
        dbAPI.fill_products(self.myDB)
        dbAPI.fill_order_history(self.myDB)
        dbAPI.fill_orders(self.myDB)
        return 
        
    #remove DB 
    def tearDown(self):
        #attempt to delete database 
        try:
            os.remove(self.myDB) 
        #show if there's an error deleting the database
        except Exception as e:
            print ("Could not delete database ", e)

    def test_get_cart_for_customer(self):
        
        result = dbAPI.get_cart_for_customer(self.myDB, customer_id=102)

        expected = [{'name': 'Chicken Wings Dish', 'quantity': 2, 'price': 9.0, 'total_price': 19}, {'name': 'Brewhouse Surface', 'quantity': 4, 'price': 24.0, 'total_price': 96}]

        self.assertEqual(result, expected)

    def test_make_order(self):
        conn = sqlite3.connect(self.myDB)
        c = conn.cursor()

        #run the function for customer 103 who has a pending order currently 
        result = dbAPI.make_order(self.myDB, customer_id=102)

        #check that the order status (and shipping status?) were updated
        #order id for pending order is 3
        data = c.execute("SELECT order_status FROM order_history_table WHERE id_order = 3 ")
        status = data.fetchone()[0]
        self.assertEqual(status,'Open')

        #check that inventory was updated
        data.execute("SELECT product_inv FROM prod_table WHERE id_product = 12")
        chicken = data.fetchone()[0]
        data.execute("SELECT product_inv FROM prod_table WHERE id_product = 18")
        brewhouse = data.fetchone()[0]
        #make sure chicken = 12-2 and brewhous equals 6-4
        self.assertEqual(chicken, 10)
        self.assertEqual(brewhouse, 2)

        conn.commit()
        conn.close()

        #make sure success message returned 
        self.assertIn("has been marked as Received", result)


if __name__ == '__main__':
    unittest.main()

