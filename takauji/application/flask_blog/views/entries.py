#ブラウザでサーバーに対してリクエストがあった時の動作をまとめている（ユーザーが起こしたアクションに対してどうこたえるか）
# エントリー（ブログの投稿機能）に関する決めごとを決める（viewsと同一ファイルにまとめてもok）
#Pythonは関数を使ってHTMLを呼び出すことが役割
from flask import request, redirect,url_for,render_template,flash,session
from flask_blog import app
from flask_blog.models.entries import Entry
from flask_blog import db
from flask_blog.views.views import login_required
from decimal import Decimal, ROUND_HALF_UP

@app.route('/') #app.routeはURLの指定
@login_required
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    sss=Entry.query.order_by(Entry.id.desc()).all() #ブログのデータが入ってるリスト
    return render_template('entries/index.html',entries=sss) #entriesという変数にユーザーの入力データを入れて、index.htmlに渡す

@app.route('/entries',methods=['POST'])
@login_required
def add_entry(): #url_forで指定された関数を呼び出す
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

#新規登録画面
@app.route('/entries/new',methods=['GET']) #ブラウザから'/entries/new'のURLを指定されたら
@login_required
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html') #entries/new.htmlというページを開く

@app.route('/aaaa',methods=['GET']) #ブラウザから'/entries/new'のURLを指定されたら
@login_required
def aaaa():

    return render_template('entries/aaaa.html') #entries/new.htmlというページを開く

#詳細画面を見る
@app.route('/entries/<int:id>',methods=['GET'])
@login_required
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry.query.get(id)
    return render_template('entries/show.html',entry=entry)

#編集画面を返す
@app.route('/entries/<int:id>/edit',methods=['GET'])
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html',entry=entry)

#フォームに入力された編集内容を受け取りデータベースを更新する
@app.route('/entries/<int:id>/update',methods=['POST'])
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title=request.form['title']
    entry.text=request.form['text']
    db.session.merge(entry)
    db.session.commit() 
    # commitでデータベースの変更を確定する
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete',methods=['POST'])
def delete_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry=Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))


###給与計算ページ＃＃＃
#入力された値をcalc_salaryに渡す
@app.route('/calc_salary',methods=['GET'])
def calc_salary():
    return render_template('entries/calc_salary.html',entry="entry") 
    # entry="entry"で値を渡してる

#給与計算の結果を表示
@app.route('/calc_result',methods=['POST']) #送信されたデータがここに送られてくる
def calc_result():
    salary=int(request.form['salary'])#formにsalaryというnameの付いた値が来るよ（HTML側から来た値を受け取れる）
    #１００万円以上なら税率が２０%
    if salary> 1000000:
        tax_amount = (salary - 1000000) * 0.2 + 100000
        tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    #それ以外なら税率が１０%  
    else:
        tax_amount = salary*0.1
        tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    pay_amount = salary - tax_amount

    print("支給額:" + str(pay_amount)+"、税額:" + str(tax_amount))

    return render_template('entries/calc_result.html',salary=salary,pay_amount=pay_amount,tax_amount=tax_amount)