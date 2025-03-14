import sqlite3

def init_db():
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Register
                           (fullname TEXT, dob TEXT, gender TEXT, address TEXT, email TEXT, mobile TEXT, usertype TEXT, username TEXT, password TEXT);''')
        db.commit()

def register_user(data):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO Register (fullname, dob, gender, address, email, mobile, usertype, username, password)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
        db.commit()

def validate_login(username, password):
    with sqlite3.connect('Library.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Register WHERE username=? AND password=?', (username, password))
        return cursor.fetchone()
