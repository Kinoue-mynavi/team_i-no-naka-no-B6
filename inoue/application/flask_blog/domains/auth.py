from flask import session
from flask_blog import app

# セッション

AUTH_FLAG = 'logged_in'

def delete_session():
    session.pop(AUTH_FLAG, None)

def create_session():
    session.permanent = True 
    session[AUTH_FLAG] = True

def get_session():
    return session.get(AUTH_FLAG)

# ログイン

def is_valid_user_name(user_name):
    return user_name == app.config['USERNAME']

def is_valid_password(password):
    return password == app.config['PASSWORD']
