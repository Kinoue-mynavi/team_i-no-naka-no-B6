from flask import render_template, flash, request, redirect, url_for
from src import app
from src.service.holiday import get_all_holidays, upsert_holiday, delete_holiday
from src.validation.holiday import is_empty, is_exceeded, DEFAULT_TEXT_MAX_LENGTH

@app.route('/')
def show_entry():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def operate_holiday():
    method_value = request.form["button"]

    params_holi_date = request.form["holi_date"]
    params_holi_text = request.form["holi_text"]

    if (is_empty(params_holi_date)):
        flash("日付が入力されていません")
        return render_template("index.html")

    if (is_empty(params_holi_text)):
        flash("日付のテキストが入力されていません")
        return render_template("index.html")

    if (is_exceeded(params_holi_text)):
        flash(f"日付のテキストは{DEFAULT_TEXT_MAX_LENGTH}文字以内で入力してください")
        return render_template("index.html")
    

    if method_value == "upsert": # Method: Create, Update
        upsert_holiday(params_holi_date, params_holi_text)
        flash("更新しましたぁ！！！！！！")

        return redirect(url_for("show_list"))

    if method_value == "delete": # Method: Delete
        status = delete_holiday(params_holi_date)

        if (status == "200"):
            flash("削除しましたぁ！！！！！！")
            return redirect(url_for("show_list"))

        flash(f"{params_holi_date}は、祝日マスタに登録されていません")

    return render_template("index.html")

@app.route("/list/")
def show_list():
    return render_template("list.html", holidays=get_all_holidays())
