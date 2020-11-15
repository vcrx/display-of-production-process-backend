from datetime import datetime
from typing import List

import arrow
from flask import request

from app.models import Yjl, YjlInfo, CyInfo, BjControl, RgControl, Hs, Sshc
from app.schemas import YjlSchema, BjControlSchema, YjlInfoSchema, \
    RgControlSchema, HsSchema, SshcSchema
from app.utils import response, get_query, safe_int
from . import front


# 首页数据
@front.route("/index_data", methods=["GET"])
def index_data():
    """
    返回参数说明：
    yjl：润叶加料
    sssf：生丝水分
    cy：储叶时长
    qs：切丝
    ------------------------------------------------
    {
        "yjl":{
            "rksf": {
                value: number,
                up: number,
                down: number,
            },   //入口水分
            "wlljzl":...,  //物料累积重量
            "cssll":...,  //物料瞬时流量
            "lywd":...,  //料液温度
            "ljjsl":...,  //累积加水量
            "ssjsl":...,  /瞬时加水量
            "wd":...,  // 环境温度
            "sd":...,  // 环境湿度
            "ckwd":...,  //出口温度
            "cksf":...,  //出口水分
            time:
        },
        "sssf":{
            "yc_sssf"：number //预测的生丝水分值
        },
        "cy":{
            "cysc",number, //储叶时长
            "wd",{
                value: number,
                up: number,
                down: number,
            }, //温度
            "sd",{
                value: number,
                up: number,
                down: number,
            } //湿度
        },
        "qs":{
            "wd":{
                value: number,
                up: number,
                down: number,
            }, //温度
            "sd":{
                value: number,
                up: number,
                down: number,
            }, //湿度
            "qssc":number //切丝时长
        },
        "time":timestamp
    }
    """
    data = {
        "yjl": {},
        "sssf": {},
        "sshc": {},
        "cy": {},
        "qs": {},
        "time": int(datetime.timestamp(datetime.now())),
    }
    bj_control: BjControl = BjControl.get_last_one()
    bj_dumped: dict = BjControlSchema().dump(bj_control)
    
    yjl: Yjl = Yjl.get_last_one()
    yjl_dumped: dict = YjlSchema().dump(yjl)
    yjl_dct = {}
    for attr, value in yjl_dumped.items():
        if attr == "time":
            yjl_dct["time"] = {
                "value": arrow.get(value).timestamp,
            }
        else:
            yjl_dct[attr] = {
                "value": value,
                "up": bj_dumped.get("yjl_{}up".format(attr)),
                "down": bj_dumped.get("yjl_{}down".format(attr)),
            }
    data["yjl"] = yjl_dct
    
    sshc = Sshc.get_last_one()
    sshc_dumped = SshcSchema().dump(sshc)
    sshc_dct = {}
    for attr, value in sshc_dumped.items():
        if attr == "time":
            sshc_dct["time"] = {
                "value": arrow.get(value).timestamp,
            }
        else:
            sshc_dct[attr] = {
                "value": value,
                "up": bj_dumped.get("sshc_{}up".format(attr)),
                "down": bj_dumped.get("sshc_{}down".format(attr)),
            }
    data["sshc"] = sshc_dct
    
    hs = Hs.get_last_one()
    hs_dumped = HsSchema().dump(hs)
    sssf_dct = {
        "time": {
            "value": arrow.get(hs_dumped["time"]).timestamp,
        },
        "sssf": {
            "value": hs_dumped["sssf"],
            "up": bj_dumped.get("sssf_up"),
            "down": bj_dumped.get("sssf_down"),
        }
    }
    data["sssf"] = sssf_dct
    
    # 储叶时长
    data["cy"]["sc"] = {
        "value": None,
        "up": None,
        "down": None,
    }
    # 储叶温度
    data["cy"]["wd"] = {
        "value": None,
        "up": bj_dumped.get("cy_wdup"),
        "down": bj_dumped.get("cy_wddown"),
    }
    # 储叶湿度
    data["cy"]["sd"] = {
        "value": None,
        "up": bj_dumped.get("cy_sdup"),
        "down": bj_dumped.get("cy_sddown"),
    }
    # 切丝温度
    data["qs"]["wd"] = {
        "value": None,
        "up": bj_dumped.get("qs_wdup"),
        "down": bj_dumped.get("qs_wddown"),
    }
    # 切丝湿度
    data["qs"]["sd"] = {
        "value": None,
        "up": bj_dumped.get("qs_sdup"),
        "down": bj_dumped.get("qs_sddown"),
    }
    return response(data=data)


@front.route("/alarm", methods=["GET"])
def alarm():
    """
    [{
        "time":timestamp,
        "pp":str, //pp:品牌
        "pch": str, //批次号
        "scjd": str, //生产阶段
        "ysys": str, //影响因素
        "bjyy": str, //报警原因
        "sfyd": str //是否以读
    }]
    """
    return response()


@front.route("/factor/<name>", methods=["GET"])
def factor(name):
    """
    生丝水分控制的影响因素：
        name可选值:
            sshc:松散回潮
            yjl:润叶加料
            cy:储叶
            qs:切丝
            hs:生丝水分
    """
    query_params = get_query(request.args)
    page = query_params.get("page", 1)
    page = safe_int(page, 1)
    per_page = query_params.get("per_page", 10)
    per_page = safe_int(per_page, 1)
    if name == "sshc":
        # 生丝水分
        data = Sshc.query.order_by(Sshc.time.desc()).paginate(page=page,
                                                              per_page=per_page,
                                                              max_per_page=20)
        items = SshcSchema(many=True).dump(data.items)
        resp_dict = {"items": items, "page": data.page,
                     "pages": data.pages, "per_page": data.per_page,
                     "total": data.total}
        return response(data=resp_dict)
    elif name == "yjl":
        # 润叶加料
        data = Yjl.query.order_by(Yjl.time.desc()).paginate(page=page,
                                                            per_page=per_page,
                                                            max_per_page=20)
        items = YjlSchema(many=True).dump(data.items)
        resp_dict = {"items": items, "page": data.page,
                     "pages": data.pages, "per_page": data.per_page,
                     "total": data.total}
        return response(data=resp_dict)
    elif name == "cy":
        # 储叶
        return response(code=500, msg="未实现")
    elif name == "qs":
        # 切丝
        return response(code=500, msg="未实现")
    elif name == "hs":
        # 生丝水分
        data = Hs.query.order_by(Hs.time.desc()).paginate(page=page,
                                                          per_page=per_page,
                                                          max_per_page=20)
        items = HsSchema(many=True).dump(data.items)
        resp_dict = {"items": items, "page": data.page,
                     "pages": data.pages, "per_page": data.per_page,
                     "total": data.total}
        return response(data=resp_dict)
    else:
        return response(code=400, msg="unknown factor name")


@front.route("/first_five_batch", methods=["GET"])
def first_five_batch():
    """
    [{
        "pph": str, // 品牌号
        "pch": str, //批次号
        ...
    }]
    """
    yjls: List[YjlInfo] = YjlInfo.query.order_by(YjlInfo.id.desc()).slice(0, 5)
    
    # [{'pph': '利群(新版)烟丝', 'pch': 195, 'rq': '2020-05-31', 'ljjsl': 58.1}, ...]
    yjl_dcts = YjlInfoSchema(many=True,
                             only=("pch", "rq", "pph", "ljjsl")).dump(yjls)
    result = []
    
    def f(name):
        return list(map(lambda x: x[name], yjl_dcts))
    
    sssfs = (
        CyInfo.query.filter(CyInfo.rq.in_(f("rq")))
            .filter(CyInfo.pph.in_(f("pph")))
            .filter(CyInfo.pch.in_(f("pch")))
            .with_entities(CyInfo.sssf)
            .order_by(CyInfo.id.desc())
            .all()
    )
    # [ {'sssf': 18.5307}, {'sssf': 18.5465}, ...]
    sssf_dcts = [dict(zip(i.keys(), i)) for i in sssfs]
    for yjl, sssf in zip(yjl_dcts, sssf_dcts):
        yjl["sssf"] = sssf["sssf"]
        yjl["rq"] = arrow.get(yjl["rq"]).format("YYYY-MM-DD")
        result.append(yjl)
    return response(data=result)


@front.route("/manual_control", methods=["GET", "PUT", "PATCH"])
def manual_control():
    """
    GET 是获取动作
        返回一个 JSON：
        {
            "ljjsl": 100,  # 累计加水量
            "sssf": 100,  # 生丝水分控制
            "cysc": 100  # 储叶时长
        }
    PUT 和 PATCH 是修改动作
        接受一个 JSON：
        {
            "ljjsl": 100,  # 累计加水量
            "sssf": 100,  # 生丝水分控制
            "cysc": 100  # 储叶时长
        }
    """
    last = RgControl.get_last_one()
    
    if request.method == "GET":
        resp = RgControlSchema().dump(last)
        return response(data=resp)
    
    data = request.get_json()
    err = RgControlSchema().validate(data)
    ljjsl = None
    sssf = None
    cysc = None
    
    # 实现 partial 更新，即只传需要改变的值即可
    if request.method == "PATCH" and last:
        ljjsl = last.ljjsl
        sssf = last.sssf
        cysc = last.cysc
    
    if not err:
        ljjsl = data.get("ljjsl", ljjsl)
        sssf = data.get("sssf", sssf)
        cysc_str = data.get("cysc")
        if cysc_str:
            cysc = arrow.get(cysc_str).datetime
        
        RgControl.add_one(ljjsl=ljjsl, sssf=sssf, cysc=cysc)
        return response()
    else:
        return response(code=400, msg=err)
