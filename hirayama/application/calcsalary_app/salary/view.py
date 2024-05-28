from flask import request,redirect,url_for,render_template,flash,session
from salary import app
from decimal import Decimal,ROUND_HALF_UP
@app.route('/')
def show_entries():
    return render_template('input.html')
@app.route('/input',methods=['GET','POST'])
def keisan():
    if request.method=='POST':
        salary=int(request.form['salary'])
        if salary <= 1000000:
            tax=salary*0.1
        else:
            over=salary-1000000
            tax=over*0.2
            tax=tax+1000000*0.1   
        tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        sala="{:,}".format(salary)
        sum="{:,}".format(salary-tax)
        zei="{:,}".format(tax)
        message="給与：{0}の場合、支給額:{1}円、税額：{2}円です。".format(sala,sum, zei)
    return render_template('output.html',salary=message)
@app.route('/',methods=['GET','POST'])
def back_page():
    return render_template('input.html')