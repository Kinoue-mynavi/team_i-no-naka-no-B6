from flask import jsonify, redirect, session, request
from flask_blog import app

users = [
   {
      "id": 1,
      "name": "Michael",
      "age": 28
   },
   {
      "id": 2,
      "name": "Steve",
      "age": 31
   },
   {
      "id": 3,
      "name": "Gomez",
      "age": 23
   },
]

@app.route("/api/")
def api_endpoint():
   return jsonify({ "status": 200 })

@app.route('/api/users')
def api_users():
   return jsonify({ "users": users, "status": 200 })

@app.route("/api/login/", methods=["POST"])
def api_login():
    if request.method != "POST":
        return jsonify({ "status": 400 })

    user_name = request.form['username']
    password = request.form['password']
    if user_name == app.config["USERNAME"] or password == app.config["PASSWORD"]:
        session.permanent = True
        session["logged_in"] = "logged_in"
        return jsonify({ "status": 201, "message": "logged_in!!" })

@app.route("/api/logout/")
def api_logout():
      session.pop("logged_in", None)
      return jsonify({ "message": "logout" })