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

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from app.config import init_config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(mode) -> Flask:
    app = Flask(__name__)
    init_config(app)
    db.init_app(app)
    ma.init_app(app)
    if mode == "app":
        CORS(app)
        from app.admin import admin as admin_blueprint  # noqa: E402
        from app.front_api import front as front_blueprint  # noqa: E402

        app.register_blueprint(admin_blueprint)
        app.register_blueprint(front_blueprint)

        @app.errorhandler(404)
        def page_not_found(error):
            return render_template("admin/404.html"), 404

    return app
