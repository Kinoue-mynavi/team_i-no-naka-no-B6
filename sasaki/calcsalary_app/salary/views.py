from flask import request, redirect, url_for, render_template, flash, session
from salary import app
import re

@app.route('/')
def show_entries():

    if session.get('salary'):   # session変数がある場合はvalueに値を入れる
        return render_template('input.html', value=session['salary'])
    
    return render_template('input.html')



# input.htmlからのリクエスト
@app.route('/input', methods=['GET', 'POST'])
def value_check():

    if request.method == 'POST':
        input_salary = request.form['inputsalary']
        session['salary'] = input_salary

        # バリデーション
        if re.fullmatch('[0-9]+', input_salary) == None:
            flash('給与は数値で入力してください。')
            return redirect('/')

        if len(input_salary) == 0:
            flash('給与が未入力です。入力してください。')
            return redirect('/')

        if len(input_salary) > 10:
            flash('給与には最大9,999,999,999まで入力可能です。')
            return redirect('/')

        if int(input_salary) < 0:
            flash('給与にはマイナスの値は入力できません。')
            return redirect('/')
        
        return redirect(url_for('calc'))
    


# 計算処理
@app.route('/output',methods=['GET','POST'])
def calc():

    TAX_UP_THRESHHOLD = 1000000     # 税額が上がる閾値
    tax_result = 0      # 税額を格納する変数の初期化
    salary = float(session['salary'])

    if salary > TAX_UP_THRESHHOLD:
        tax_result += (salary-TAX_UP_THRESHHOLD)*0.2 + TAX_UP_THRESHHOLD*0.1
    else:
        tax_result += salary*0.1

    return render_template('output.html', 
                           salary = "{:,}".format(round(salary)), 
                           paid = "{:,}".format(round(salary-tax_result)),
                           tax = "{:,}".format(round(tax_result)))



# ルートへ帰還
@app.route('/back')
def back_route():
    return redirect('/')