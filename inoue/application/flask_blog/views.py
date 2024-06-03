from flask import request, redirect, url_for, render_template, flash
from flask_blog import app
from flask_blog.domains.auth import get_session, create_session, delete_session, is_valid_password, is_valid_user_name
from flask_blog.domains.entries import get_all_entries, create_entry
from functools import wraps

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not get_session(): # ログインして「いない」場合
            flash("ログインが必要です")
            return redirect(url_for("show_login"))
        return view(*args, **kwargs) # ログインして「いる」場合
    return inner

@app.route('/')
@login_required
def show_entries():
    entries = get_all_entries()
    return render_template('entries/index.html', entries=entries)

@app.route('/login/')
def show_login():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    if request.method != 'POST':
        flash("400: 不正なリクエストが送信されました", "alert-danger")

    auth_params_user_name = request.form['username']
    auth_params_password = request.form['password']

    if not is_valid_user_name(auth_params_user_name):
        flash('ユーザー名が異なります')
    elif not is_valid_password(auth_params_password):
        flash('パスワードが異なります')
    else:
        create_session()
        flash('ログインしました', "alert-success") 
        return redirect(url_for('show_entries'))

    return render_template('login.html')

@app.route('/logout/')
def logout():
    delete_session()
    flash('ログアウトしました', "alert-info")
    return redirect(url_for('show_entries'))

@app.route('/new/')
def show_new():
    return render_template("new.html")

@app.route('/new/', methods=["POST"])
def new():
    if request.method != 'POST':
        flash("400: 不正なリクエストが送信されました", "alert-danger")
        return render_template("new.html")
    
    params_text = request.form['text']
    params_title = request.form['title']

    create_entry(params_title, params_text)

    return redirect(url_for("show_entries"))

