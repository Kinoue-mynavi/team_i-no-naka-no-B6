## セットアップ

1. `/inoue`ディレクトリにいることを確認する

```shell
pwd
```

2. Flask-Blogの起動

```shell
make run-blog
```

3. Flask-BlogのDBマイグレーション

```shell
make db-migrate
```

4. 給与計算アプリの起動

```shell
make run-salary
```

5. クライアントプロジェクトの起動

```shell
make run-c
```

## Python 開発環境

```shell
Package           Version
----------------- ------------
click             8.0.4
cryptography      39.0.2
Flask             1.1.2
Flask-Script      2.0.6
Flask-SQLAlchemy  2.5.1
greenlet          1.1.2
itsdangerous      2.0.1
MarkupSafe        2.1.
Jinja2            3.0.3
PyMySQL           1.0.2
setuptools        54.2.0
SQLAlchemy        1.4.3
Werkzeug          2.0.3
```