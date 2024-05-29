from flask import request, redirect,url_for,render_template,flash,session
from salary import app
from decimal import Decimal,ROUND_HALF_UP

@app.route('/', methods['GET','POST'])
def input():
    input_data=session.get('input_data',None)
    return render_template("input.html",input=input_data)

@app.route('/output',methods=['GET','POST'])
def output():
    session["input_data"]=""
