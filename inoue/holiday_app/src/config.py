import os 

SQLALCHEMY_DATABASE_URI="mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
    **{
        "user": os.getenv("DB_USER","root"),
        "password": os.getenv("DB_PASSWORD","mysql"),
        "host": os.getenv("DB_HOST","localhost"),
        "database": os.getenv("DB_DATABASE","ENSHU")
    }
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
SECRET_KEY = os.urandom(12)
USERNAME = "testUser"
PASSWORD = "password"
