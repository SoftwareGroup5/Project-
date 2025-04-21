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

    # Test for add to cart - Cole
    def test_add_to_processing_cart(self):
        # Add 1 of product ID 1 (Treering Counter) to customer 102's cart
        dbAPI.add_to_processing_cart(self.myDB, 102, 1, 1)

        # Retrieve updated cart for customer 102
        result = dbAPI.get_cart_for_customer(self.myDB, 102)

        # Check that the new item is in the cart along with the existing items
        expected_names = {'Chicken Wings Dish', 'Brewhouse Surface', 'Treering Counter'}
        result_names = {item['name'] for item in result}

        self.assertEqual(result_names, expected_names)

        # Find the new item and check its quantity and total
        for item in result:
            if item['name'] == 'Treering Counter':
                self.assertEqual(item['quantity'], 1)
                self.assertEqual(item['price'], 14.99)
                self.assertEqual(item['total_price'], round(14.99, 2))



if __name__ == '__main__':
    unittest.main()

