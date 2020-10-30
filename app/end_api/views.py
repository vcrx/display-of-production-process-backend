from . import end
from app.utils import response
from flask import request

# 获取报警信息
@end.route("/get_alert", methods=["GET"])
def end_get_alert():
    query_type = request.args.get("type")
    return response()


# 修改报警信息
@end.route("/modify_alert", methods=["POST"])
def end_get_alert():
    query_type = request.get_json()
    return response()
