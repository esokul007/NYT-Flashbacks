import sqlite3, os
from flask import Flask, request, render_template, redirect, url_for, flash, session
import api_handling

app = Flask(__name__)
app.secret_key = os.urandom(32)

def setup():
    try:
        with sqlite3.connect('api_info.db') as conn:
            info = api_handling.addDB()
            c= conn.cursor()
            for i in info:
                year = i[0]
                event = i[1]
                c.execute("INSERT INTO events(event, year) VALUES(?, ?)", (event, year))
    except sqlite3.IntegrityError:
        flash("Database Error")
def init_db():
    conn = sqlite3.connect('api_info.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT UNIQUE NOT NULL,
    year TEXT NOT NULL)
    ''')
    setup()
    conn.commit()
    conn.close

def get_events():
    try:
        with sqlite3.connect('api_info.db') as conn:
            c = conn.cursor()
            events = c.execute("SELECT event, year FROM events ORDER BY RANDOM()").fetchmany(20)
            return(events)
    except sqlite3.IntegrityError:
        print('Database Error')
        