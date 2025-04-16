#author stephen tynan
#purpose: host static html
from flask import Flask, render_template, request, redirect, url_for, session

import dbAPI
import os, sqlite3

app = Flask(__name__, static_folder='static')
app.secret_key = 'development_secret_key_12345'

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
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

def print_auth_table():
    conn = sqlite3.connect('countertops_demo.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    c = conn.cursor()
    
    # Query the auth_table
    c.execute('SELECT * FROM auth_table')
    rows = c.fetchall()
    
    # Format the results as HTML
    result = '<h2>Auth Table Contents</h2>'
    result += '<table border="1"><tr><th>ID</th><th>Password</th><th>Auth Level</th><th>Auth Status</th><th>Customer ID</th><th>Products Owned</th></tr>'
    
    for row in rows:
        result += f'<tr>'
        result += f'<td>{row["id_login"]}</td>'
        result += f'<td>{row["pass_login"]}</td>'
        result += f'<td>{row["auth_level"]}</td>'
        result += f'<td>{row["auth"]}</td>'
        result += f'<td>{row["customer_id"]}</td>'
        result += f'<td>{row["products_owned"]}</td>'
        result += f'</tr>'
    
    result += '</table>'
    conn.close()
    print(result)
    
    return result

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
    return 'customer profile'

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

@app.route('/debug/auth_table')
def debug_auth_table():
    conn = sqlite3.connect('countertops_demo.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    c = conn.cursor()
    
    # Query the auth_table
    c.execute('SELECT * FROM auth_table')
    rows = c.fetchall()
    
    # Format the results as HTML
    result = '<h2>Auth Table Contents</h2>'
    result += '<table border="1"><tr><th>ID</th><th>Password</th><th>Auth Level</th><th>Auth Status</th><th>Customer ID</th><th>Products Owned</th></tr>'
    
    for row in rows:
        result += f'<tr>'
        result += f'<td>{row["id_login"]}</td>'
        result += f'<td>{row["pass_login"]}</td>'
        result += f'<td>{row["auth_level"]}</td>'
        result += f'<td>{row["auth"]}</td>'
        result += f'<td>{row["customer_id"]}</td>'
        result += f'<td>{row["products_owned"]}</td>'
        result += f'</tr>'
    
    result += '</table>'
    conn.close()
    
    return result

if __name__ == '__main__':
    app.run(debug=True)