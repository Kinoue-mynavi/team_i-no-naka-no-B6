from flask import request, redirect,url_for,render_template,flash,session
from holiday import app
from holiday.models.entries import Holiday
from holiday import db
from decimal import Decimal, ROUND_HALF_UP


#データベースからデータを一覧取得して返す
@app.route('/') #app.routeはURLの指定
def show_entries():
    # sss=Entry.query.order_by(Entry.id.desc()).all() #ブログのデータが入ってるリスト
    holidays=Holiday.query.all() #Holidaysのデータを全取得できる
    return render_template('entries/index.html',holidays=holidays) #entriesという変数にユーザーの入力データを入れて、index.htmlに渡す