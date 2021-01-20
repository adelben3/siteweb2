# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:11:42 2021

@author: Gaben
"""
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Thiago', password='vitrygtr'))
users.append(User(id=2, username='admin', password='pass'))
users.append(User(id=3, username='Gaben', password='halflife3'))


app = Flask(__name__,static_folder='static')
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return render_template('loginfaux.html')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')
    
@app.route('/analyses', methods=['GET', 'POST'])
def analyses():

    return render_template('analyses.html')

@app.route('/infos', methods=['GET', 'POST'])
def infos():

    return render_template('infos.html')