from . import end
from app.utils import response
from flask import request
from app.models import BjControl
from app import db


def safe_float(value, default):
    try:
        return float(value)
    except Exception:
        return default


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
    if type == "ryjl":
        obj = BjControl()
        obj.yjl_rksfup = safe_float(data.get("rksf-up"), 0)
        obj.yjl_rksfdown = safe_float(data.get("rksf-down"), 0)
        obj.yjl_cljzlup = safe_float(data.get("wlljzl-up"), 0)
        obj.yjl_cljzldown = safe_float(data.get("wlljzl-down"), 0)
        obj.yjl_ssjslup = safe_float(data.get("ssjsl-up"), 0)
        obj.yjl_ssjsldown = safe_float(data.get("ssjsl-down"), 0)
        obj.yjl_lywdup = safe_float(data.get("lywd-up"), 0)
        obj.yjl_lywddown = safe_float(data.get("lywd-down"), 0)
        obj.yjl_wdup = safe_float(data.get("hjwd-up"), 0)
        obj.yjl_wddown = safe_float(data.get("hjwd-down"), 0)
        obj.yjl_sdup = safe_float(data.get("hjsd-up"), 0)
        obj.yjl_sddown = safe_float(data.get("hjsd-down"), 0)
        obj.yjl_ckwdup = safe_float(data.get("ckwd-up"), 0)
        obj.yjl_ckwddown = safe_float(data.get("ckwd-down"), 0)
        obj.yjl_cksfup = safe_float(data.get("cksf-up"), 0)
        obj.yjl_cksfdown = safe_float(data.get("cksf-down"), 0)
        db.session.add(obj)
        db.session.commit()
        return response()
    elif type == "sshc":
        return response()
    else:
        return response(code=404, msg="unknown type")
