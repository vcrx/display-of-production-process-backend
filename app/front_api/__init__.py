from flask import Blueprint

front = Blueprint("front", __name__, url_prefix="/front")

from .views import *  # noqa: E402
