#author stephen tynan
#purpose: host static html
from flask import Flask, render_template
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
    #need to set a session variable customer_id so we can add to + display cart on other pages 
        
    return 'login'

@app.route('/cart')
def cart():
    
    #customer_id = session.get('customer_id')
    #cart_items = dbAPI.get_cart_for_customer(DB_NAME, customer_id)
    
    cart_items= [{'name': 'Chicken Wings Dish', 'quantity': 2, 'price': 9.0, 'total_price': 19}, {'name': 'Brewhouse Surface', 'quantity': 4, 'price': 24.0, 'total_price': 96}]
    cart_total = sum(item['total_price'] for item in cart_items)

    return render_template('cart.html', cart_items=cart_items, cart_total=cart_total)
    

@app.route('/profile_client')
def profile_client():
    return 'client profile'

@app.route('/profile_cust')
def profile_cust():
    return 'customer profile'


if __name__ == '__main__':
    app.run(debug=True)