#author stephen tynan
#purpose: host static html
from flask import Flask, render_template, request, redirect, url_for

import dbAPI

app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return 'products'

@app.route('/login')
def login():
    #once logged in, we need to set a session variable customer_id so we can add to + display cart on other pages 
        
    return 'login'

@app.route('/cart', methods=['GET', 'POST'])
def cart():

    if request.method == 'POST':
        #dbAPI.make_order()
        dbAPI.make_order('countertops_demo.db', 103)  #make the order 
        return redirect(url_for('cart'))  #refresh the page after making the order

    #customer_id = session.get('customer_id')
    #cart_items = dbAPI.get_cart_for_customer('countertops_demo.db', customer_id)
    
    #two variables to pass into the template: cart_items and cart_total
    cart_items= [{'name': 'Chicken Wings Dish', 'quantity': 2, 'price': 9.0, 'total_price': 19}, {'name': 'Brewhouse Surface', 'quantity': 4, 'price': 24.0, 'total_price': 96}]
    cart_total = sum(item['total_price'] for item in cart_items)

    return render_template('cart.html', cart_items=cart_items, cart_total=cart_total)
    

@app.route('/profile_client')
def profile_client():
    return 'client profile'

@app.route('/profile_cust')
def profile_cust():
    return 'customer profile'

@app.route('/portal')
def portal():
    db_path = 'countertops_demo.db'
    
    inventory_data = dbAPI.get_store_inventory(db_path)
    shipping_data = dbAPI.get_shipping_status(db_path)
    
    return render_template(
        'portal.html',
        inventory=inventory_data,
        shipping=shipping_data
    )


# Checks on the db
def delete_db(db):
    if os.path.exists(db):
        os.remove(db)
        return f"Database '{db}' deleted"
    else:
        return f"Database '{db}' does not exist"


# Creates the dev database for this demo ### must run this before demo ###
@app.route('/fill_test_data')
def fill_test_data():
    db_path = 'countertops_demo.db'
    
    delete_status = dbAPI.delete_db(db_path)
    dbAPI.create(db_path)
    
    autho = dbAPI.fill_auth(db_path)
    customer_status = dbAPI.fill_customers(db_path)
    products_list = dbAPI.fill_products(db_path)
    order_history = dbAPI.fill_order_history(db_path)
    orders_status = dbAPI.fill_orders(db_path)


    return f"{autho}<br>{customer_status}<br>{products_list}<br>{order_history}<br>{orders_status}"

if __name__ == '__main__':
    app.run(debug=True)