from . import end
from app.utils import response
from flask import request
from app.models import BjControl
from app import db


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
@end.route("/modify_alert/<type>", methods=["POST"])
def end_modify_alert(type):
    """
    form 请求
    根据 type 判断是修改的哪部分的报警
    松散回潮：
    润叶加料：
        rksf-up: 入口水分上限
        rksf-down: 入口水分下限
        wlljzl-up: 物料累计重量上限
        wlljzl-down: ...
        ssjsl-up: 瞬时加水量上限
        ssjsl-down:
        lywd-up: 料液温度上限
        lywd-down:
        hjwd-up: 环境温度上限
        hjwd-down:
        hjsd-up: 环境湿度上限
        hjsd-down:
        ckwd-up: 出口温度上限
        ckwd-down:
        cksf-up: 出口水分上限
        ckwd-down:

    返回参数
        {
            "status":str,
            "code":200 //200为成功，其它为失败
        }
    """
    data = request.form
    print(data)
    
    print(type)
    if type == "yjl":
        obj = BjControl()
        obj.yjl_rksfup = data.get("rksf-up")
        obj.yjl_rksfdown = data.get("rksf-down")
        obj.yjl_cljzlup = data.get("wlljzl-up")
        obj.yjl_cljzldown = data.get("wlljzl-down")
        obj.yjl_ssjslup = data.get("ssjsl-up")
        obj.yjl_ssjsldown = data.get("ssjsl-down")
        obj.yjl_lywdup = data.get("lywd-up")
        obj.yjl_lywddown = data.get("lywd-down")
        obj.yjl_wdup = data.get("hjwd-up")
        obj.yjl_wddown = data.get("hjwd-down")
        obj.yjl_sdup = data.get("hjsd-up")
        obj.yjl_sddown = data.get("hjsd-down")
        obj.yjl_ckwdup = data.get("ckwd-up")
        obj.yjl_ckwddown = data.get("ckwd-down")
        obj.yjl_cksfup = data.get("cksf-up")
        obj.yjl_cksfdown = data.get("cksf-down")
        db.session.add(obj)
        db.session.commit()
        return response()
    elif type == "sshc":
        return response()
    else:
        return response(code=404, msg="unknown type")
