from flask_blog import app
from flask import request, render_template, redirect

# html
@app.route("/")
def show_entries():
   return render_template("entries/index.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
            if request.form["username"] != app.config["USERNAME"]:
                print("ユーザー名が異なります")
            elif request.form["password"] != app.config["PASSWORD"]:
                print("パスワードが異なります")
            else:
                return redirect("/")
    
    return render_template("/login.html")

@app.route("/logout/")
def logout():
     return redirect("/index.html")
