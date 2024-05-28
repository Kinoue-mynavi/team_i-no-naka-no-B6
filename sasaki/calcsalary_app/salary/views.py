from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def calc():
    input_salary = float(request.form['inputsalary'])
    result = 0
    if input_salary > 1000000:
        result += (input_salary-1000000)*0.2 + 1000000*0.1
    else:
        result += input_salary*0.1
    return render_template('output.html', 
                           salary = "{:,}".format(round(input_salary)), 
                           paid = "{:,}".format(round(input_salary-result)),
                           tax = "{:,}".format(round(result)))
