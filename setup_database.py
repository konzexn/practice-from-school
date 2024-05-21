# setup_database.py
import sqlite3

conn = sqlite3.connect('personal_info.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE personal_info (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, occupation TEXT, bio TEXT)''')
c.execute('''CREATE TABLE favorite_foods (id INTEGER PRIMARY KEY, name TEXT, image_url TEXT)''')
c.execute('''CREATE TABLE favorite_animals (id INTEGER PRIMARY KEY, name TEXT, image_url TEXT)''')

# Insert data
c.execute("INSERT INTO personal_info (name, age, occupation, bio) VALUES ('ChatGPT', 2, 'AI Assistant', 'I am a large language model trained by OpenAI.')")
c.execute("INSERT INTO favorite_foods (name, image_url) VALUES ('Pizza', 'https://example.com/pizza.jpg')")
c.execute("INSERT INTO favorite_foods (name, image_url) VALUES ('Sushi', 'https://example.com/sushi.jpg')")
c.execute("INSERT INTO favorite_animals (name, image_url) VALUES ('Cat', 'https://example.com/cat.jpg')")
c.execute("INSERT INTO favorite_animals (name, image_url) VALUES ('Dog', 'https://example.com/dog.jpg')")

conn.commit()
conn.close()
