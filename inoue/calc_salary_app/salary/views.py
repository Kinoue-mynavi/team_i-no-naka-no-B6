import math
from salary import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def calc_salary():
    salary = int(request.form['salary'])

    amount = calc_amount(salary)
    allowance = amount["allowance"]
    tax_amount = amount["tax_amount"]

    result = f"給与：{salary}、税額：{ tax_amount }、支給額：{ allowance }"

    # 結果のテキストを丸ごと返す
    return render_template(
        "output.html",
        result=result
    )

@app.route("/output/")
def output():
    return render_template("output.html")      

MAX_AMOUNT = 1000000
def calc_amount(salary: int):
    tax_amount = salary * 0.1 if salary <= MAX_AMOUNT else MAX_AMOUNT * 0.1 + (salary - MAX_AMOUNT) * 0.2
    allowance = salary - tax_amount

    return {
        "tax_amount": math.floor(tax_amount),
        "allowance": math.floor(allowance),
    }
