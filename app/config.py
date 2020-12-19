from flask import Flask
from app.constants import mysql_uri
from os import getenv as _env


def init_config(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri
    # ECHO 如果设置成 True，SQLAlchemy 将会标准输出(stderr)记录语句，这对调试很有帮助。
    app.config["SQLALCHEMY_ECHO"] = False
    # 禁用以提高性能
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = _env("SECRET_KEY")
