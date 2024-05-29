from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import flask_blog.views

app.config.from_object("flask_blog.config")
app.secret_key = app.config["SECRET_KEY"]
