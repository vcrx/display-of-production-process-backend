from flask import request

from app import db
from app.models import BjControl
from app.utils import response, safe_float
from . import end


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
    if type == "ryjl":
        obj = BjControl.get_last_one() or BjControl()
        obj.yjl_rksfup = safe_float(data.get("yjl_rksfup"), 0)
        obj.yjl_rksfdown = safe_float(data.get("yjl_rksfdown"), 0)
        obj.yjl_wlljzlup = safe_float(data.get("yjl_wlljzlup"), 0)
        obj.yjl_wlljzldown = safe_float(data.get("yjl_wlljzldown"), 0)
        obj.yjl_ssjslup = safe_float(data.get("yjl_ssjslup"), 0)
        obj.yjl_ssjsldown = safe_float(data.get("yjl_ssjsldown"), 0)
        obj.yjl_lywdup = safe_float(data.get("yjl_lywdup"), 0)
        obj.yjl_lywddown = safe_float(data.get("yjl_lywddown"), 0)
        obj.yjl_wdup = safe_float(data.get("yjl_wdup"), 0)
        obj.yjl_wddown = safe_float(data.get("yjl_wddown"), 0)
        obj.yjl_sdup = safe_float(data.get("yjl_sdup"), 0)
        obj.yjl_sddown = safe_float(data.get("yjl_sddown"), 0)
        obj.yjl_ckwdup = safe_float(data.get("yjl_ckwdup"), 0)
        obj.yjl_ckwddown = safe_float(data.get("yjl_ckwddown"), 0)
        obj.yjl_cksfup = safe_float(data.get("yjl_cksfup"), 0)
        obj.yjl_cksfdown = safe_float(data.get("yjl_cksfdown"), 0)
        db.session.add(obj)
        db.session.commit()
        return response()
    elif type == "sshc":
        obj = BjControl.get_last_one() or BjControl()
        obj.sshc_cksfup = safe_float(data.get("sshc_cksfup"), 0)
        obj.sshc_cksfdown = safe_float(data.get("sshc_cksfdown"), 0)
        db.session.add(obj)
        db.session.commit()
        return response()
    elif type == "cy":
        obj = BjControl.get_last_one() or BjControl()
        obj.cy_wdup = safe_float(data.get("cy_wdup"), 0)
        obj.cy_wddown = safe_float(data.get("cy_wddown"), 0)
        obj.cy_sdup = safe_float(data.get("cy_sdup"), 0)
        obj.cy_sddown = safe_float(data.get("cy_sddown"), 0)
        db.session.add(obj)
        db.session.commit()
        return response()
    elif type == "qs":
        obj = BjControl.get_last_one() or BjControl()
        obj.qs_wdup = safe_float(data.get("qs_wdup"), 0)
        obj.qs_wddown = safe_float(data.get("qs_wddown"), 0)
        obj.qs_sdup = safe_float(data.get("qs_sdup"), 0)
        obj.qs_sddown = safe_float(data.get("qs_sddown"), 0)
        db.session.add(obj)
        db.session.commit()
        return response()
    else:
        return response(code=404, msg="unknown type")
