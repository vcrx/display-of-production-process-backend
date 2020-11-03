from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1/yancao"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "7edb4f4bf4324848b0c68a3a4c6e3543"
app.debug = True
db = SQLAlchemy(app)
CORS(app)
from app.admin import admin as admin_blueprint  # noqa: E402
from app.front_api import front as front_blueprint  # noqa: E402
from app.end_api import end as end_blueprint  # noqa: E402

app.register_blueprint(admin_blueprint)
app.register_blueprint(front_blueprint)
app.register_blueprint(end_blueprint)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("admin/404.html"), 404
