#Managerというモジュールをインポート
from flask_script import Manager
from flask_blog import app
from flask_brog.scripts.db import InitDB

#スクリプトファイルの登録
if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db',InitDB()) #
    manager.run()    