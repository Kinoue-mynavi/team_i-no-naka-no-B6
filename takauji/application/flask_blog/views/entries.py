from flask import request, redirect,url_for,render_template,flash,session
from flask_blog import app
from flask_blog.models.entries import Entry

@app.route('/entries/new',methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        return render_template('entries/new.html')

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        return render_template('entries/index.html')

