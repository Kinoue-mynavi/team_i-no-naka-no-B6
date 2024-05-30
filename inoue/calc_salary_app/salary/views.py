import math
from salary import app
from flask import render_template, request, flash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def calc_salary():
    input_salary = request.form['salary']

    # validation
    # FIXME: render_template("index.html")を共通化する
    if (is_empty(input_salary)):
        flash("給与が未入力です。入力してください。")
        return render_template("index.html")
    
    if (is_exceeded(input_salary)):
        flash("給与には最大9,999,999,999まで入力可能です")
        return render_template("index.html")

    if (is_minus(input_salary)):
        flash("給与にはマイナスの値は入力できません")
        return render_template("index.html")

    salary = int(input_salary)

    amount = calc_amount(salary)
    allowance = amount["allowance"]
    tax_amount = amount["tax_amount"]

    result = f"給与：{salary}、税額：{tax_amount}、支給額：{allowance}"

    # 結果のテキストを丸ごと返す
    return render_template(
        "output.html",
        result=result
    )  

MAX_AMOUNT = 1000000
def calc_amount(salary: int):
    tax_amount = salary * 0.1 if salary <= MAX_AMOUNT else MAX_AMOUNT * 0.1 + (salary - MAX_AMOUNT) * 0.2
    allowance = salary - tax_amount

    return {
        "tax_amount": math.floor(tax_amount),
        "allowance": math.floor(allowance),
    }

def is_empty(input_salary: str) -> bool:
    return True if not input_salary else False
    
def is_exceeded(input_salary: str) -> bool:
    return True if len(input_salary) > 9 else False

def is_minus(input_salary: str) -> bool:
    return True if int(input_salary) < 0 else False

