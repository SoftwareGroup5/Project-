import sqlite3
import os

#I'm assuming we want to put all the tables in one create function but we don't have to...?
def create (db):
    #set up connection
    conn = sqlite3.connect(db)
    #set up connection cursor 
    c = conn.cursor()
    #create orders table
    c.execute("""CREATE TABLE IF NOT EXISTS orders (
              order_id INT,
              product_id INT, 
              quantity INT NOT NULL, 
              total_price DECIMAL(10,2),
              PRIMARY KEY (order_id, product_id),
              FOREIGN KEY (product_id) REFERENCES products(id_product),
              FOREIGN KEY (order_id) REFERENCES order_history(id_order)
             );""")
    #create trigger so orders table calculates total price whenever a new item added 
    #c.execute("""CREATE TRIGGER calculate_total_price
            #AFTER INSERT ON orders
            #FOR EACH ROW
            #BEGIN
              #UPDATE orders
              #SET total_price = NEW.quantity * (SELECT unit_price FROM products WHERE products.id_product = NEW.product_id)
              #WHERE order_id = NEW.order_id;
            #END;
             #);""")
    
    ### more tables .....
    c.execute("""CREATE TABLE IF NOT EXISTS auth_table (
                  id_login VARCHAR(25),
                  pass_login VARCHAR(25),
                  auth_level VARCHAR(5),
                  auth BOOLEAN,
                  customer_id INT,
                  products_owned TEXT,
                  PRIMARY KEY (id_login),
                  FOREIGN KEY (customer_id) REFERENCES order_history(id_order)
            );""")
    conn.commit()
    conn.close()
    
    return 


    #create prod_table to store product data
    c.execute("""CREATE TABLE IF NOT EXISTS prod_table (
                  id_product INT PRIMARY KEY,
                  prod_name TEXT,
                  img_link TEXT,
                  prod_price FLOAT,
                  product_inv INT
            );""")
    
    conn.commit()
    conn.close()
    
    return 




#this can be a fill for all tables or we can do 1 per table and then call them all in the test file, doesn't matter to me -nicole
#right now its specific for the orders table

def fill_orders (db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    #add entries to orders, this is tested in test_dbAPI which just makes sure it populates values 
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (1, 1, 1)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (1, 2, 2)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (2, 3, 3)")
    
    conn.commit()
    conn.close()
    return 

def fill_auth(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    test_value_auth = [
        ('admin', 'root', 'client', False, 0, 'all'), 
        ('test_cust', 'test', 'cust', False, 1, 'none'), 
        ('test_client', 'test', 'client', False, 2, 'test')
        ]
    c.executemany(''' INSERT INTO auth_table
                      ( id_login, pass_login, auth_level, auth, customer_id, products_owned )
                      VALUES (?, ?, ?, ?, ?, ?)''', test_value_auth)            
    conn.commit()
    conn.close()
    return "DB auth_table filled with sample data"


def fill_products(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    test_value_prod = [
        #(id_product ,product name,image link, product price, product inventory, product inv) 
        # Nature
        (1, 'Treering Counter', 'Project-/Images/Nature/treering.png', 14.99, 10),
        (2, 'Leaf Branches Decor', 'Project-/Images/Nature/leaf branches.webp', 11.25, 8),
        (3, 'Jungle-Themed Kitchen', 'Project-/Images/Nature/jungle-themed-kitchen.png', 25.50, 5),
        (4, 'Sinkhole Basin', 'Project-/Images/Nature/sinkhole.png', 30.00, 4),
        (5, 'Water Moss Texture', 'Project-/Images/Nature/water moss.webp', 13.45, 6),
        (6, 'Snowy Counter', 'Project-/Images/Nature/snowycounter.png', 18.75, 9),
        (7, 'Mountain Design', 'Project-/Images/Nature/mountains.png', 22.00, 3),

        # Animal
        (8, 'Leopard Print Plate', 'Project-/Images/Animal/leopard.png', 19.95, 7),
        (9, 'Elephant-Themed Kitchen', 'Project-/Images/Animal/elephant-themed-kitchen.png', 29.99, 5),
        (10, 'Panda Print Tray', 'Project-/Images/Animal/panda.png', 16.25, 6),
        (11, 'Puppy Mug', 'Project-/Images/Animal/puppy.png', 12.99, 10),

        # JunkFood
        (12, 'Chicken Wings Dish', 'Project-/Images/JunkFood/chicken_wings.png', 9.50, 12),
        (13, 'Potato Chip Plate', 'Project-/Images/JunkFood/potatoe_chip.png', 7.25, 15),
        (14, 'French Fries Bowl', 'Project-/Images/JunkFood/french_fries.png', 8.99, 14),
        (15, 'Cheese Sticks Tray', 'Project-/Images/JunkFood/cheese_sticks.png', 10.50, 9),

        # Industrial
        (16, 'Concrete Texture', 'Project-/Images/Industrial/concrete.webp', 13.00, 8),
        (17, 'CS Countertop', 'Project-/Images/Industrial/ComputerScienceCounter.png', 27.75, 4),
        (18, 'Brewhouse Surface', 'Project-/Images/Industrial/brewhouse.png', 24.00, 6),
        (19, 'Brick Design Panel', 'Project-/Images/Industrial/brick.png', 20.50, 5),
        (20, 'Steel Factory Look', 'Project-/Images/Industrial/stainless-steel-factory.png', 31.25, 3),
        (21, 'Bikeshop Bar', 'Project-/Images/Industrial/bikeshop.png', 23.99, 7)
    ]
    c.executemany(''' INSERT INTO prod_table
                      ( id_product, prod_name, img_link, prod_price, product_inv )
                      VALUES (?, ?, ?, ?, ?)''', test_value_prod)
    conn.commit()
    conn.close()
    return "DB prod_table filled with sample data"

#functions
def addOrders(db, order_id, product_id, quantity):
    #write this later - need to pull from other tables 
    return 


#functions for login
def authorize(db, user, user_pass):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''SELECT *
                FROM auth_table
                WHERE id_login = ? AND pass_login = ?''', (user, user_pass))
    res = c.fetchall()
    id_login, pass_login, auth_level, auth, customer_id, products_owned = res[0]
    c.execute('''UPDATE auth_table
                 SET auth = TRUE
                 WHERE id_login = ? AND pass_login = ?''', (user, user_pass))
    auth = True
    return id_login, auth_level, auth, customer_id, products_owned

#function for deletion
def delete_db(db):
    if os.path.exists(db):
        os.remove(db)
        return f"Database '{db}' deleted"
    else:
        return f"Database '{db}' does not exist"
    
    



    
    

