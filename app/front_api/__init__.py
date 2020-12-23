import os
from pathlib import Path
from flask import Blueprint, send_from_directory

front = Blueprint("front", __name__, url_prefix="/front")

react_folder = (
    Path(os.path.dirname(os.path.realpath(__file__))) / ".." / Path("react_app")
)

# Serve React App
@front.route("/", defaults={"path": ""})
@front.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(react_folder / path):
        return send_from_directory(str(react_folder.absolute()), path)
    else:
        return send_from_directory(str(react_folder.absolute()), "index.html")


from .views import *  # noqa: E402
