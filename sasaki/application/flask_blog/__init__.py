from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import flask_blog.views

app.config.from_object('flask_blog.config')

db = SQLAlchemy

import flask_blog.views