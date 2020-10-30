from . import front
from app.utils import response
from flask import request

# 首页数据
@front.route("/get_index_data", methods=["GET"])
def get_index_data():
    return response()


# 生丝水分控制的影响因素：
@front.route("/get_influence", methods=["GET"])
def front_get_influence():
    query_type = request.args.get("type")
    return response()
