from flask import Blueprint

end = Blueprint("end", __name__)
from .views import *  # noqa: E402
