from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1/sssf"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "7edb4f4bf4324848b0c68a3a4c6e3543"

app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from app.front_api import front as front_blueprint

app.register_blueprint(home_blueprint, url_prefix='/admin')
app.register_blueprint(admin_blueprint)
app.register_blueprint(front_blueprint,url_prefix='/front')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("admin/404.html"), 404


