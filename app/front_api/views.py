from . import front
from app.utils import response
from flask import request
from app.models import Yjl, Hs, Sshc
from datetime import datetime


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
            "yjl_rksf":number,   //入口水分
            "yjl_cljzl":number,  //物料累积重量
            "yjl_cssll":number,  //物料瞬时流量
            "yjl_lywd":number,  //料液温度
            "yjl_ljjsl":number,  //累积加水量
            "yjl_ssjsl":number,  /瞬时加水量
            "yjl_wd":number,  // 环境温度
            "yjl_sd":number,  // 环境湿度
            "yjl_ckwd":number,  //出口温度
            "yjl_cksf":number,  //出口水分
            "yjlsc":number  //叶加料时长
        },
        "sssf":{
            "yc_sssf"：number //预测的生丝水分值
        },
        "cy":{
            "cysc",number, //储叶时长
            "cy_wd",number, //温度
            "cy_sd",number //湿度
        },
        "qs":{
            "qs_wd":number, //温度
            "qs_sd":number, //湿度
            "qssc":number //切丝时长
        },
        "time":timestamp
    }
    """
    data = {"yjl": {}, "sssf": {}, "cy": {}, "qs": {},
            "time": int(datetime.timestamp(datetime.now()))}
    yjl: Yjl = Yjl.query.order_by(Yjl.id.desc()).first()
    data["yjl"]["wlsjll"] = yjl.wlsjll
    data["yjl"]["wlljzl"] = yjl.wlljzl
    data["yjl"]["ljjsl"] = yjl.ljjsl
    data["yjl"]["rksf"] = yjl.rksf
    data["yjl"]["ssjsl"] = yjl.ssjsl
    data["yjl"]["ssjlj"] = yjl.ssjlj
    data["yjl"]["lywd"] = yjl.lywd
    data["yjl"]["ckwd"] = yjl.ckwd
    data["yjl"]["cksf"] = yjl.cksf
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
