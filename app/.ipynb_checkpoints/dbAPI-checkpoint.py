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
              FOREIGN KEY (product_id) REFERENCES prod_table(id_product),
              FOREIGN KEY (order_id) REFERENCES order_history_table(id_order)
             );""")
    
        #customer_table
    c.execute("""CREATE TABLE IF NOT EXISTS customer_table (
                  id_customer INT PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  address TEXT
            );""")

    
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

    #create prod_table to store product data
    c.execute("""CREATE TABLE IF NOT EXISTS prod_table (
                  id_product INT PRIMARY KEY,
                  prod_name TEXT,
                  img_link TEXT,
                  prod_price FLOAT,
                  product_inv INT
            );""")
    
    #create prod_table to store product data
    c.execute("""CREATE TABLE IF NOT EXISTS order_history_table (
                  id_order INTEGER PRIMARY KEY,
                  customer_id INTEGER,
                  order_status TEXT,
                  date TEXT,
                  shipping_status TEXT,
                  FOREIGN KEY (customer_id) REFERENCES customer_table(id_customer)
            );""")
    
    conn.commit()
    conn.close()
    
    return 



#this can be a fill for all tables or we can do 1 per table and then call them all in the test file, doesn't matter to me -nicole
#right now its specific for the orders table

def fill_orders (db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    # added more rows to line up with order_history
    #add entries to orders, this is tested in test_dbAPI which just makes sure it populates values 
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (1, 1, 1)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (1, 2, 2)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (2, 3, 3)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (2, 4, 3)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (2, 5, 3)")
    c.execute("INSERT INTO orders (order_id,product_id,quantity) VALUES (2, 6, 3)")
    
    conn.commit()
    conn.close()
    return 

# Modified fill value to match customer_table ids
def fill_auth(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    test_value_auth = [
        ('admin', 'root', 'client', False, 101, 'all'), 
        ('test_cust', 'test', 'cust', False, 102, 'none'), 
        ('test_client', 'test', 'client', False, 103, 'test')
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

def fill_order_history(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    test_order_history = [
        ('1', '101', 'Open', '2025/01/02', 'Shipped'),
        ('2', '102', 'Closed', '2024/01/02', 'Received'),
        ('3', '103', 'Processing', '2025/03/28', 'Pending'),
        ('4', '101', 'Open', '2025/01/02', 'Staged'),
        ('5', '102', 'Closed', '2024/06/02', 'Received'),
        ('6', '103', 'Closed', '2024/08/02', 'Received')
        ]
    c.executemany(''' INSERT INTO order_history_table
                      ( id_order, customer_id, order_status, date, shipping_status )
                      VALUES (?, ?, ?, ?, ?)''', test_order_history)            
    conn.commit()
    conn.close()
    return "DB order_history filled with sample data"

 
def fill_customers(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    test_value_customers = [
        (101, 'John', 'Doe', '123 Maple St'),
        (102, 'Jane', 'Smith', '456 Oak Rd'),
        (103, 'Alex', 'Taylor', '789 Pine Ln')
    ]
    c.executemany('''
        INSERT INTO customer_table (id_customer, first_name, last_name, address)
        VALUES (?, ?, ?, ?)
    ''', test_value_customers)
    conn.commit()
    conn.close()
    return "DB customer_table filled with sample data"

#functions
def fill_orders(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    insert_order(db, 1, 3, 1)
    insert_order(db, 1, 2, 1)
    insert_order(db, 2, 1, 1)
    insert_order(db, 3, 18, 4)
    insert_order(db, 3, 12, 2)
    insert_order(db, 4, 5, 10)

    conn.commit()
    conn.close()
    return 


def insert_order(db, order_id, product_id, quantity):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #get the unit price for product
    c.execute("SELECT prod_price FROM prod_table WHERE id_product = ?", (product_id,))
    result = c.fetchone()
    unit_price = result[0]
    total_price = quantity * unit_price

    # Insert into orders with total_price calculated
    c.execute("INSERT INTO orders (order_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)",
              (order_id, product_id, quantity, total_price))

    conn.commit()
    conn.close()
    return

def get_cart_for_customer(DB, customer_id):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Get the current pending order ID for this customer
    c.execute("""
        SELECT id_order FROM order_history_table
        WHERE customer_id = ? AND shipping_status = 'Pending'
    """, (customer_id,))
    result = c.fetchone()

    if not result:
        conn.close()
        return []

    order_id = result['id_order']

    # Get cart items from orders + product name
    c.execute("""
        SELECT p.prod_name AS name,
               o.quantity,
               ROUND(o.total_price / o.quantity, 2) AS price,  -- price per unit
               o.total_price
        FROM orders o
        JOIN prod_table p ON o.product_id = p.id_product
        WHERE o.order_id = ?
    """, (order_id,))

    cart_items = [dict(row) for row in c.fetchall()]
    conn.close()
    return cart_items




def get_customer_by_id(db, customer_id):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT id_customer, first_name, last_name, address FROM customer_table WHERE id_customer = ?", (customer_id,))
    customer = c.fetchone()
    conn.close()
    return customer



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
    

# Retrieve all products for listing page
def get_all_products(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''
        SELECT id_product, prod_name, img_link, prod_price, product_inv 
        FROM prod_table
    ''')
    products = [dict(row) for row in c.fetchall()]
    conn.close()
    return products


# Retrieve one product by ID
def get_product_by_id(db, product_id):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''
        SELECT prod_name, img_link, prod_price, product_inv 
        FROM prod_table 
        WHERE id_product = ?
    ''', (product_id,))
    result = c.fetchone()
    conn.close()
    return dict(result) if result else None


# inventory chart in customer portal
def get_store_inventory(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('''
        SELECT 
            p.id_product,
            p.prod_name,
            p.img_link,
            p.product_inv,
            COALESCE(SUM(o.quantity), 0) AS open_orders
        FROM prod_table AS p
        LEFT JOIN orders AS o ON p.id_product = o.product_id
        LEFT JOIN order_history_table AS oh 
            ON o.order_id = oh.id_order AND oh.order_status = 'Open'
        GROUP BY p.id_product, p.prod_name, p.img_link, p.product_inv;
        ''')
    products = [dict(row) for row in c.fetchall()]
    
    # calculating the stock
    
    c.execute("SELECT SUM(product_inv) AS total_stock FROM prod_table")
    row = c.fetchone()
    total_stock = row["total_stock"] if row and row["total_stock"] is not None else 0
    
    conn.close()
    
    return {"products": products, "total_stock": total_stock}


def get_shipping_status(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''
        SELECT oh.date AS ship_date,
            COALESCE(GROUP_CONCAT(p.prod_name, ', '), '') AS products,
            (c.first_name || ' ' || c.last_name) AS customer_name,
            c.address,
            oh.shipping_status
        FROM order_history_table oh
        JOIN customer_table c ON oh.customer_id = c.id_customer
        LEFT JOIN orders o ON oh.id_order = o.order_id
        LEFT JOIN prod_table p ON o.product_id = p.id_product
        GROUP BY oh.id_order, oh.date, customer_name, c.address, oh.shipping_status
        ORDER BY oh.date;
        ''')
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return {"data": rows}
    

