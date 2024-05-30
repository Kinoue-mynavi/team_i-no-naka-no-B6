#事前に定義したDBモジュールをインポート
from flask_script import Command
from flask_blog import db
#モデルに指定したEntryをインポート
from flask_blog.models.entries import Entry

#InitDBというクラスを定義
class InitDB(Command):
    "create database"

#このクラスを定義
    def run(self):
        db.create_all()
