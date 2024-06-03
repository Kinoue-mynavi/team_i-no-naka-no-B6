#一度設定したら変わることのない設定するよ（データベースを定義したり、シークレットキーを設定したり）
#ここに書くことはほぼほぼコピペが多い
DEBUG=True
SECRET_KEY='secret key'
USERNAME='John'
PASSWORD='due123' #ユーザー名やパスワードは通常ここで設定することはない

import os

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user":os.getenv("DB_USER","root"),
    "password" :os.getenv("DB_PASSWORD","mysql"),
    "host":os.getenv("DB_HOST","localhost"),
    "database":os.getenv("DB_DATABASE","ENSHU")
    })
SQLALCHEMY_TRACK_MODIFICATIONS=False