from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/input',methods=['GET','POST'])
def value_check():
    input_salary = request.form["inputsalary"]
    if input_salary == "":
        flash('給与が未入力です。入力してください。')
        return render_template("input.html")
        
    if len(input_salary) >11:
        flash('給与には最大9,999,999,999まで入力可能です。')
        return render_template("input.html")

    if int(input_salary) < 0:
        flash('給与にはマイナスの値は入力できません。')
        return render_template("input.html")

    salary=int(input_salary)
    result = 0
    if salary > 1000000:
        result += (salary-1000000)*0.2 + 1000000*0.1
    else:
        result += salary*0.1
    return render_template('output.html', 
                           salary = "{:,}".format(round(salary)), 
                           paid = "{:,}".format(round(salary-result)),
                           tax = "{:,}".format(round(result)))

# # @app.route('/output',methods=['GET','POST'])
# def calc():
#     input_salary = float(request.form['inputsalary'])
#     result = 0
#     if input_salary > 1000000:
#         result += (input_salary-1000000)*0.2 + 1000000*0.1
#     else:
#         result += input_salary*0.1
#     return render_template('output.html', 
#                            salary = "{:,}".format(round(input_salary)), 
#                            paid = "{:,}".format(round(input_salary-result)),
#                            tax = "{:,}".format(round(result)))