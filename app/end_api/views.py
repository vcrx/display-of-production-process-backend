from . import end
from app.utils import response
from flask import request


# 获取报警信息
@end.route("/get_alert", methods=["GET"])
def end_get_alert():
    """
    Query参数：type[str]
    type 可选值为：
        sshc:松散回潮
        yjl:润叶加料
        cy:储叶
        qs:切丝
        sssf:生丝水分
    """
    query_type = request.args.get("type")
    return response()


# 修改报警信息
@end.route("/modify_alert", methods=["POST"])
def end_modify_alert():
    """
    body请求参数：json
        {
            "process":type,
            "value":[{
                    "ysys":str,
                    "up":number,
                    "down":number,
            },
            ...
        }
    返回参数
        {
            "status":str,
            "code":200 //200为成功，其它为失败
        }
    """
    data = request.get_json()
    return response()
