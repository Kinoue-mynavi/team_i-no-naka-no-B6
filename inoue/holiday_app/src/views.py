from flask import redirect, url_for, render_template, flash, session
from src import app
from functools import wraps

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get["logged_in"]: # ログインして「いない」場合
            flash("ログインが必要です")
            return redirect(url_for("show_login"))
        return view(*args, **kwargs) # ログインして「いる」場合
    return inner

@app.route('/')
def show_entry():
    return render_template("index.html")

@app.route("/list/")
def show_list():
    return render_template("list.html")