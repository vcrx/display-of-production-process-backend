from flask import Blueprint
from flask.templating import render_template

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
    template_folder="../templates",
)


@admin.errorhandler(404)
def page_not_found(error):
    return render_template("admin/404.html"), 404


import app.admin.views  # noqa: F401
