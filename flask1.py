from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import os
from hashlib import scrypt

# Helper function to hash passwords
def hash_password(password):
    return scrypt(password.encode(), salt=os.urandom(16), n=2**14, r=8, p=1).hex()

def initialize_database():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT, price REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, product TEXT, price REAL, date TEXT)''')

    # Populate products table
    products = [
        ('Laptop', 500),
        ('Mouse', 20),
        ('Keyboard', 30)
    ]
    for product in products:
        c.execute('INSERT OR IGNORE INTO products (product, price) VALUES (?, ?)', product)

    # Populate users table with hashed passwords and roles
    users = [
        ('admin', hash_password('adminpass'), 'admin'),
        ('seller', hash_password('sellerpass'), 'seller'),
        ('customer', hash_password('customerpass'), 'customer')
    ]
    for user in users:
        try:
            c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', user)
        except sqlite3.IntegrityError:
            # User already exists, ignore this entry
            pass

    conn.commit()
    conn.close()

# Initialize the database
initialize_database()

app = Flask(__name__)
app.secret_key = 'super secret key'

DATABASE = 'store.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def hash_password(password):
    return scrypt(password.encode(), salt=os.urandom(16), n=2**14, r=8, p=1).hex()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
        if user and user[1] == hash_password(password):
            session['username'] = username
            session['role'] = user[2]
            return redirect(url_for('dashboard'))
        else:
            return 'Incorrect credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        hashed_password = hash_password(password)
        db = get_db()
        try:
            db.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', [username, hashed_password, role])
            db.commit()
        except sqlite3.IntegrityError:
            return 'Username already exists'
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        if session['role'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif session['role'] == 'seller':
            return redirect(url_for('seller_dashboard'))
        elif session['role'] == 'customer':
            return redirect(url_for('customer_dashboard'))
    return redirect(url_for('login'))

@app.route('/admin')
def admin_dashboard():
    if 'username' in session and session['role'] == 'admin':
        users = query_db('SELECT username, role FROM users')
        products = query_db('SELECT * FROM products')
        transactions = query_db('SELECT * FROM transactions')
        return render_template('admin_dashboard.html', users=users, products=products, transactions=transactions)
    return 'Access Denied'

@app.route('/seller')
def seller_dashboard():
    if 'username' in session and session['role'] == 'seller':
        products = query_db('SELECT * FROM products')
        transactions = query_db('SELECT * FROM transactions')
        return render_template('seller_dashboard.html', products=products, transactions=transactions)
    return 'Access Denied'

@app.route('/customer')
def customer_dashboard():
    if 'username' in session and session['role'] == 'customer':
        products = query_db('SELECT * FROM products')
        return render_template('customer_dashboard.html', products=products)
    return 'Access Denied'

@app.route('/admin/manage_users', methods=['POST'])
def manage_users():
    if 'username' in session and session['role'] == 'admin':
        action = request.form['action']
        username = request.form['username']
        db = get_db()
        if action == 'delete':
            db.execute('DELETE FROM users WHERE username = ?', [username])
        db.commit()
        return redirect(url_for('admin_dashboard'))
    return 'Access Denied'

@app.route('/admin/manage_products', methods=['POST'])
def manage_products():
    if 'username' in session and session['role'] == 'admin':
        action = request.form['action']
        product_id = request.form['product_id']
        db = get_db()
        if action == 'delete':
            db.execute('DELETE FROM products WHERE id = ?', [product_id])
        db.commit()
        return redirect(url_for('admin_dashboard'))
    return 'Access Denied'

@app.route('/seller/manage_products', methods=['POST'])
def seller_manage_products():
    if 'username' in session and session['role'] == 'seller':
        action = request.form['action']
        product_id = request.form['product_id']
        db = get_db()
        if action == 'delete':
            db.execute('DELETE FROM products WHERE id = ?', [product_id])
        db.commit()
        return redirect(url_for('seller_dashboard'))
    return 'Access Denied'

@app.route('/customer/buy', methods=['POST'])
def buy():
    if 'username' in session and session['role'] == 'customer':
        product_id = request.form['product_id']
        db = get_db()
        product = query_db('SELECT * FROM products WHERE id = ?', [product_id], one=True)
        db.execute('INSERT INTO transactions (username, product, price, date) VALUES (?, ?, ?, datetime())', 
                   [session['username'], product[1], product[2]])
        db.commit()
        return redirect(url_for('customer_dashboard'))
    return 'Access Denied'

if __name__ == '__main__':
    app.run(debug=True)