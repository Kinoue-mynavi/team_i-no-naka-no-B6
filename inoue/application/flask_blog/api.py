from flask import jsonify
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
def endpoint():
   return jsonify({ "status": "success" })

@app.route('/api/users')
def get_all_users():
   return jsonify({ "users": users, "status": "success" })
