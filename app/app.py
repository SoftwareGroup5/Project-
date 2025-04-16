#author stephen tynan
#purpose: host static html
from flask import Flask, render_template, request, redirect, url_for, session

import dbAPI
import os, sqlite3

app = Flask(__name__, static_folder='static')
app.secret_key = 'notsosecretkey'

@app.context_processor
def inject_user():
    """Make user session data available to all templates"""
    return dict(
        logged_in=session.get('logged_in', False),
        auth_level=session.get('auth_level', None),
        username=session.get('username', None)
    )

@app.route('/')
@app.route('/home')
def home():
    fill_test_data()
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(f"Login attempt: username={username}, password={password}")
        
        # Check if the database file exists
        if not os.path.exists('countertops_demo.db'):
            error = "Database not found. Please set up the demo data first."
            print(f"Database error: {error}")
            return render_template('login.html', error=error)
        
        try:
            # Print auth table for debugging
            print("Auth table content before login attempt:")
            conn = sqlite3.connect('countertops_demo.db')
            c = conn.cursor()
            c.execute('SELECT * FROM auth_table')
            rows = c.fetchall()
            for row in rows:
                print(row)
            conn.close()
            
            # Call the authorize function to verify credentials
            id_login, auth_level, auth, customer_id, products_owned = dbAPI.authorize('countertops_demo.db', username, password)
            
            print(f"Login successful: id={id_login}, level={auth_level}, auth={auth}, customer_id={customer_id}")
            
            # Store user information in session
            session['logged_in'] = True
            session['username'] = id_login
            session['auth_level'] = auth_level
            session['customer_id'] = customer_id
            session['products_owned'] = products_owned
            
            # Redirect based on auth level
            if auth_level == 'client':
                return redirect(url_for('profile_client'))
            else:
                return redirect(url_for('profile_cust'))
                
        except Exception as e:
            # If login fails, show error message
            print(f"Login error: {str(e)}")
            error = f"Login failed: {str(e)}"
    
    # GET request or login failed
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for('home'))

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
    

@app.route('/profile_cust')
def profile_cust():
    # Check if user is logged in and is a customer
    if not session.get('logged_in') or session.get('auth_level') != 'cust':
        return redirect(url_for('login'))
    
    # Get the user profile data
    profile = {
        'username': session.get('username'),
        'auth_level': session.get('auth_level'),
        'customer_id': session.get('customer_id'),
        'products_owned': session.get('products_owned')
    }
    
    # Get additional customer details from the database
    customer_details = dbAPI.get_customer_by_id('countertops_demo.db', session.get('customer_id'))
    
    return render_template('profile_cust.html', profile=profile, customer=customer_details)

@app.route('/profile_client')
def profile_client():
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


# Runs automatically when homepage is called. can cause potential errors with db level auth resetting. session should remain.

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