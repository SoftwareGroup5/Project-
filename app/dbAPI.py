import sqlite3

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
    c.execute("""CREATE TRIGGER calculate_total_price
            AFTER INSERT ON orders
            FOR EACH ROW
            BEGIN
              UPDATE orders
              SET total_price = NEW.quantity * (SELECT unit_price FROM products WHERE products.id_product = NEW.product_id)
              WHERE order_id = NEW.order_id;
            END;
             );""")
    
    ### more tables .....
    
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

def addOrders(db, order_id, product_id, quantity):
    #write this later - need to pull from other tables 
    return 