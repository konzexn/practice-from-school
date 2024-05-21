from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('personal_info.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE if not exists personal_info (name TEXT, age INTEGER, occupation TEXT, bio TEXT)''')
c.execute('''CREATE TABLE if not exists favorite_foods (id INTEGER PRIMARY KEY, name TEXT, image_url TEXT)''')
c.execute('''CREATE TABLE if not exists favorite_animals (id INTEGER PRIMARY KEY, name TEXT, image_url TEXT)''')

# Insert data
c.execute("INSERT INTO personal_info (name, age, occupation, bio) VALUES ('Erwin', 29, 'Student', 'I like playing games.')")
c.execute("INSERT INTO favorite_foods (name, image_url) VALUES ('Pizza', 'https://example.com/pizza.jpg')")
c.execute("INSERT INTO favorite_foods (name, image_url) VALUES ('Sushi', 'https://example.com/sushi.jpg')")
c.execute("INSERT INTO favorite_animals (name, image_url) VALUES ('Cat', 'https://example.com/cat.jpg')")
c.execute("INSERT INTO favorite_animals (name, image_url) VALUES ('Dog', 'https://example.com/dog.jpg')")

conn.commit()
conn.close()


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('personal_info.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    personal_info = conn.execute('SELECT * FROM personal_info').fetchone()
    conn.close()
    return render_template('home.html', name=personal_info['name'], age=personal_info['age'], occupation=personal_info['occupation'], bio=personal_info['bio'])

@app.route('/favorite_foods')
def favorite_foods():
    conn = get_db_connection()
    favorite_foods = conn.execute('SELECT * FROM favorite_foods').fetchall()
    conn.close()
    return render_template('favorite_foods.html', favorite_foods=favorite_foods)

@app.route('/favorite_animals')
def favorite_animals():
    conn = get_db_connection()
    favorite_animals = conn.execute('SELECT * FROM favorite_animals').fetchall()
    conn.close()
    return render_template('favorite_animals.html', favorite_animals=favorite_animals)

if __name__ == '__main__':
    app.run(debug=True)
