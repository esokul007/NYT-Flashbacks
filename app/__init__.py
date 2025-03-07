from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os, random, sys
import db_handling, api_handling

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'index' not in session:
        session['index'] = 0
        session['curr_event'] = api_handling.getEvent(random.randint(1, 12), random.randint(0, 200))
        session['next_event'] = api_handling.getEvent(random.randint(1, 12), random.randint(0, 200))
    lost = False
    index = session['index']

    if request.method == 'POST':
        button_pressed = request.form.get('guess')
        print(button_pressed)
        if button_pressed == 'BEFORE':
            lost = int(session['curr_event'][0]) < int(session['next_event'][0])
        elif button_pressed == 'AFTER':
            lost= int(session['next_event'][0]) < int(session['curr_event'][0])
        session['index'] += 1
        session['curr_event']=session['next_event']
        session['next_event'] = api_handling.getEvent(random.randint(1, 12),  random.randint(0, 200))
    if (lost):
        session['index'] = 0
    return render_template("home.html", curr_event=session['curr_event'], next_event=session['next_event'], i=session['index'])
'''def check_guess():
    if request.method == 'POST':
        button_pressed = request.form.get('guess')

        if button_pressed == 'before':

        elif button_pressed == 'after':'''



if __name__ == '__main__':
    app.debug = True
    app.run()