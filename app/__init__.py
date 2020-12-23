import pyodbc

"""
https://docs.sqlalchemy.org/en/14/dialects/mssql.html#pass-through-exact-pyodbc-string
PyODBC默认情况下使用内部池，这意味着连接的生存期将比SQLAlchemy本身内的连接的生存期更长。
由于SQLAlchemy有自己的池行为，通常最好禁用此行为。
在建立任何连接之前，在PyODBC模块级别全局禁用此行为。

如果将此变量保留为其默认值True，即使SQLAlchemy本身丢弃连接，python 程序也将继续维护活动的数据库连接。
"""
pyodbc.pooling = False

from dotenv import load_dotenv

load_dotenv()

from os import getenv as _env
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from .constants import mysql_uri


def init_config(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri
    # ECHO 如果设置成 True，SQLAlchemy 将会标准输出(stderr)记录语句，这对调试很有帮助。
    app.config["SQLALCHEMY_ECHO"] = False
    # 禁用以提高性能
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = _env("SECRET_KEY")

    # 是否需要从头采集 SQLServer 数据库
    app.config["SCHEDULER_COLLECTION_FROM_SCRATCH"] = False


def create_app(mode="app") -> Flask:
    app = Flask(__name__)

    init_config(app)

    db.init_app(app)
    ma.init_app(app)

    if mode == "app":
        from .admin import admin as admin_blueprint  # noqa: E402
        from .front_api import front as front_blueprint  # noqa: E402

        app.register_blueprint(admin_blueprint)
        app.register_blueprint(front_blueprint)

        CORS(app)

        @app.errorhandler(404)
        def page_not_found(error):
            return render_template("admin/404.html"), 404

        from .scheduler import init_scheduler

        init_scheduler(app)
    return app
