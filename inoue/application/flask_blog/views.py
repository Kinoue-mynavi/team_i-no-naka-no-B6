from flask_blog import app
from flask import request, render_template, redirect, session, flash

# html
@app.route("/")
def show_entries():
   if not session.get("logged_in"):
       flash("ログインが必要です")
       return redirect("/login")
   return render_template("entries/index.html")

@app.route("/login/")
def show_login():
    return render_template("/login.html")

@app.route("/login/", methods=["POST"])
def login():
    if request.method != "POST":
        flash("不正なリクエストが送信されました", "failed")
        return redirect("/")

    user_name = request.form['username']
    password = request.form['password']
    if user_name == app.config["USERNAME"] or password == app.config["PASSWORD"]:
        flash("ログインしました！", "success")
        session.permanent = True
        session["logged_in"] = "logged_in"
        return redirect("/")

@app.route("/logout/")
def logout():
    flash("ログアウトしました！")
    session.pop("logged_in", None)
    return redirect("/")
