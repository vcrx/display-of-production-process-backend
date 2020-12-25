from pathlib import Path
from flask import Blueprint, send_from_directory

front = Blueprint("front", __name__, url_prefix="/front")

react_folder = (
    Path(__file__).parent.parent / "react_app"
).absolute()

# Serve React App
@front.route("/", defaults={"path": ""})
@front.route("/<path:path>")
def serve(path):
    if path != "" and (react_folder / path).exists():
        return send_from_directory(str(react_folder), path)
    else:
        return send_from_directory(str(react_folder), "index.html")


from .views import *  # noqa: E402
