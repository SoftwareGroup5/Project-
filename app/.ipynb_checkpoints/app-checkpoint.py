#author stephen tynan
#purpose: host static html
from flask import Flask, render_template

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
    return 'login'

@app.route('/cart')
def cart():
    return 'cart'

@app.route('/profile_client')
def profile_client():
    return 'client profile'

@app.route('/profile_cust')
def profile_cust():
    return 'customer profile'


if __name__ == '__main__':
    app.run(debug=True)