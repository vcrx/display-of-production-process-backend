from datetime import datetime
from typing import List

import arrow
from flask import request

from app.models import Yjl, YjlInfo, CyInfo, BjControl, RgControl
from app.schemas import YjlSchema, BjControlSchema, YjlInfoSchema, \
    RgControlSchema
from app.utils import response
from . import front


# 首页数据
@front.route("/get_index_data", methods=["GET"])
def get_index_data():
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
        "cy": {},
        "qs": {},
        "time": int(datetime.timestamp(datetime.now())),
    }
    yjl: Yjl = Yjl.query.order_by(Yjl.id.desc()).first()
    yjl_attr_list = ("wlljzl", "rksf", "ssjsl", "lywd", "ckwd", "cksf")
    yjl_dumped = YjlSchema(only=yjl_attr_list).dump(yjl)
    bj_control: BjControl = BjControl.get_last_one()
    bj_dumped = BjControlSchema().dump(bj_control)
    print(bj_dumped)
    yjl_dct = {}
    for attr in yjl_attr_list:
        yjl_dct[attr] = {
            "value": yjl_dumped[attr],
            "up": bj_dumped.get("yjl_{}up".format(attr)),
            "down": bj_dumped.get("yjl_{}down".format(attr)),
        }
    print(yjl_dct)
    data["yjl"] = yjl_dct
    # 储叶时长
    data["cy"]["sc"] = {
        "value": "",
        "up": None,
        "down": None,
    }
    # 储叶温度
    data["cy"]["wd"] = {
        "value": "",
        "up": bj_control.cy_wdup,
        "down": bj_control.cy_wddown,
    }
    # 储叶湿度
    data["cy"]["sd"] = {
        "value": "",
        "up": bj_control.cy_sdup,
        "down": bj_control.cy_sddown,
    }
    # 切丝温度
    data["qs"]["wd"] = {
        "value": "",
        "up": bj_control.qs_wdup,
        "down": bj_control.qs_wddown,
    }
    # 切丝湿度
    data["qs"]["sd"] = {
        "value": "",
        "up": bj_control.qs_sdup,
        "down": bj_control.qs_sddown,
    }
    return response(data=data)


# 生丝水分控制的影响因素：
@front.route("/get_influence", methods=["GET"])
def front_get_influence():
    """
    type 可选值为：
        sshc:松散回潮
        yjl:润叶加料
        cy:储叶
        qs:切丝
        sssf:生丝水分
    ----------------------------------------------------
    {
        "process": type,
        "value":[
            {
                "ysys":str,
                "current_value":number,
                "range":str,
                "time": timestamp
            },
            ... //表示还有多个以上的结构
        ]
    }
    """
    query_type = request.args.get("type")
    return response()


@front.route("/get_alarm", methods=["GET"])
def front_get_alarm():
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


@front.route("/get_first_five_batch", methods=["GET"])
def get_first_five_batch():
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
        "rg_ljjsl": 100,  # 累计加水量
        "rg_sssf": 100,  # 生丝水分控制
    }
    PUT 和 PATCH 是修改动作
    接受一个 JSON：
    {
        "rg_ljjsl": 100,  # 累计加水量
        "rg_sssf": 100,  # 生丝水分控制
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
    # 实现 partial 更新，即只传需要改变的值即可
    if request.method == "PATCH":
        if last:
            ljjsl = last.rg_ljjsl
            sssf = last.rg_sssf
    
    if not err:
        ljjsl = data.get("rg_ljjsl", ljjsl)
        sssf = data.get("rg_sssf", sssf)
        RgControl.add_one(ljjsl, sssf)
        return response()
    else:
        return response(code=400, msg=err)
