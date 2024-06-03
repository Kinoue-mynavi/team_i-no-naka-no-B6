#アプリの基盤になる機能や設定のインストール、設定（ほぼコピペでok）
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #便利機能インストール

#インストールしたflaskから新しいアプリを作るよ
app=Flask(__name__)
#import flask_blog.views
app.config.from_object('flask_blog.config') #そのアプリの設定ファイルはこれだよ(Flask_blogの下にあるconfigファイル

#このアプリでデータベース（SQLAlchemy】を使うよ
db=SQLAlchemy(app)

#このアプリは、Falskblogのディレクトリの中にあるViewsディレクトリの中にあるviewsとentriesを使って動かすよ
from flask_blog.views import views,entries