from flask import Flask

app=Flask(__name__)

import salary.view

app.config.from_object("salary.config")
app.secret_key = app.config["SECRET_KEY"]