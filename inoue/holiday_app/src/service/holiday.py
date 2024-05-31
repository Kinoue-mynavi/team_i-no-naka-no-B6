from src import db
from src.models.holiday import Holiday
from flask import flash

# 単体取得
def get_holiday(holi_date): # 引数はプライマリーキー
    try: 
        return Holiday.query.get(holi_date)
    except Exception as e:
        db.session.rollback()
        print(e)
        flash('取得に失敗しました', "alert-danger")

# 一覧取得
def get_all_holidays():
    try: 
        return Holiday.query.all()
    except Exception as e:
        db.session.rollback()
        print(e)
        flash('一覧の取得に失敗しました', "alert-danger")

def create_holiday(holi_date, holi_text):
    holiday = Holiday(
        holi_date = holi_date,
        holi_text = holi_text,
    )
    db.session.add(holiday)
    db.session.commit()

# 更新・作成
def upsert_holiday(holi_date, holi_text):
    try: 
        holiday = get_holiday(holi_date)
        if not holiday:
            create_holiday(holi_date, holi_text)
        else:
            holiday.holi_text = holi_text
            db.session.merge(holiday)
            db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(e)
        flash("データの更新に失敗しました", "alert-danger")

# 削除
def delete_holiday(holi_date):
    try: 
        holiday = get_holiday(holi_date)
        if not holiday:
            return "404"
        else:
            db.session.delete(holiday)
            db.session.commit()
            return "200"
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("データの削除に失敗しました", "alert-danger")
