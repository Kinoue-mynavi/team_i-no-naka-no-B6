from flask_blog import db
from flask_blog.models.entries import Entry
from datetime import datetime
from flask import flash

def get_all_entries():
    try: 
        return Entry.query.all()
    except:
        db.session.rollback()
        print('データの取得に失敗しました')

def create_entry(title, text):
    try: 
        entry = Entry(
            title=title,
            text=text,
        )
        db.session.add(entry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("データの作成に失敗しました", "alert-success")