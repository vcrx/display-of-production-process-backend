from . import front
from app.utils import response
from flask import request
from app.models import Yjl, YjlInfo, CyInfo, BjControl
from datetime import datetime
from typing import List


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
            "cljzl":...,  //物料累积重量
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
    data = {"yjl": {}, "sssf": {}, "cy": {}, "qs": {},
            "time": int(datetime.timestamp(datetime.now()))}
    yjl: Yjl = Yjl.query.order_by(Yjl.id.desc()).first()
    bj_control: BjControl = BjControl.get_last_one()
    if bj_control:
        # 物料累计重量
        data["yjl"]["wlljzl"] = {
            "value": yjl.wlljzl,
            "up": bj_control.yjl_cljzlup,
            "down": bj_control.yjl_cljzldown,
        }
        # 入口水分
        data["yjl"]["rksf"] = {
            "value": yjl.rksf,
            "up": bj_control.yjl_rksfup,
            "down": bj_control.yjl_rksfdown,
        }
        # 瞬时加水量
        data["yjl"]["ssjsl"] = {
            "value": yjl.ssjsl,
            "up": bj_control.yjl_ssjslup,
            "down": bj_control.yjl_ssjsldown,
        }
        # 料液温度
        data["yjl"]["lywd"] = {
            "value": yjl.lywd,
            "up": bj_control.yjl_lywdup,
            "down": bj_control.yjl_lywddown,
        }
        # 出口温度
        data["yjl"]["ckwd"] = {
            "value": yjl.ckwd,
            "up": bj_control.yjl_ckwdup,
            "down": bj_control.yjl_ckwddown,
        }
        # 出口水分
        data["yjl"]["cksf"] = {
            "value": yjl.cksf,
            "up": bj_control.yjl_cksfup,
            "down": bj_control.yjl_cksfdown,
        }
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
        "pp":str, //pp:品牌
        "pch": str, //批次号
        ...
    }]
    """
    yjls: List[YjlInfo] = YjlInfo.query.order_by(YjlInfo.id.desc()).slice(0, 5)
    result = []
    for yjl in yjls:
        tmp = {}
        pch = yjl.pch
        tmp["pch"] = pch
        rq = yjl.rq
        tmp["rq"] = rq
        pp = yjl.pph
        tmp["pp"] = pp
        jsl = yjl.ljjsl
        tmp["jsl"] = jsl
        cy: CyInfo = CyInfo.query.filter(CyInfo.pch == pch, CyInfo.pph == pp,
                                         CyInfo.rq == rq).first()
        # 如果 cy 是 none， 则说明没查到
        if cy is not None:
            tmp["sssf"] = cy.sssf
        else:
            tmp["sssf"] = None
        result.append(tmp)
    return response(data=result)
