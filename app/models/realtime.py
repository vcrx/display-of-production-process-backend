from collections import defaultdict
from typing import Any, Dict

import arrow
import pandas as pd
from app import db
from app.utils.string import remove_prefix, remove_suffix
from sqlalchemy import exc

from .base import Base
from .history import SshcInfo, YjlInfo


def get_data(df):
    """
    {
        '2020/10/12 13:06': {
            'qualified': 1,
            'DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_03.OutPhyPV': {
                '_NUMERICID': 0.0,
                '_VALUE': 18.793315889,
                '_QUALITY': 192.0
            },
            ...
        },
    }
    """

    grouped_by_time = df.groupby("_TIMESTAMP")
    result = {}
    for time_str in grouped_by_time.groups.keys():
        _df = grouped_by_time.get_group(time_str)
        data = _df.groupby("_BATCHID").mean().drop("id", axis=1).T.to_dict()
        _qualified = (_df["_QUALITY"] == 192).all()
        qualified = 1 if _qualified else 0
        data["qualified"] = qualified
        time_arrow = arrow.get(time_str).datetime
        result[time_arrow] = data
    return result


UP_SUFFIX = "_up"
DOWN_SUFFIX = "_down"


def judge_limit(df, limit: dict, prefix: str, mapping: dict):
    fields = limit.keys()
    result = defaultdict(dict)

    for origin_field in fields:
        # 移除前后缀，获取字段名：如 sshc_cksf_up -> cksf
        field = remove_prefix(origin_field, prefix)
        field = remove_suffix(remove_suffix(field, UP_SUFFIX), DOWN_SUFFIX)
        name = mapping[field]
        data_dict: Dict[Any, Dict[str, Dict[str, float]]] = get_data(df)

        for time, data in data_dict.items():
            # 不是有效数据
            if not data.get("qualified"):
                continue
            dct: dict = data.get(name)
            if not dct:
                # 没这个 name 值
                break
            value = dct.get("_VALUE")
            # 上限
            if origin_field.endswith(UP_SUFFIX):
                if value > limit[origin_field]:
                    result[time][origin_field] = {
                        "reason": f"{origin_field}，上限：{limit[origin_field]} 目前：{value}",
                    }
            # 下限
            if origin_field.endswith(DOWN_SUFFIX):
                if value < limit[origin_field]:
                    result[time][origin_field] = {
                        "reason": f"{origin_field}，下限：{limit[origin_field]} 目前：{value}",
                    }
    return result


class Sshc(Base, db.Model):
    """松散回潮"""

    _mapping = {
        "wlssll": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_PV_Massflow",
        "wlljzl": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_Total_Massflow",
        "hfwd": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.TB101_PV_Temperature",
        "cksf": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Moisture",
        "ckwd": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Temp",
    }
    __tablename__ = "sshc"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    time = db.Column(db.DateTime)  # 时间
    qualified = db.Column(db.Integer, default=0)  # 质量， 1 为符合， 0 为不符合

    wlssll = db.Column(db.Float)  # 物料实时流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    hfwd = db.Column(db.Float)  # 回风温度
    ckwd = db.Column(db.Float)  # 出口温度
    cksf = db.Column(db.Float)  # 出口水分

    wd = db.Column(db.Float)  # 温度
    sd = db.Column(db.Float)  # 湿度

    sssf_controls = db.relationship("SssfControl", backref="sshc")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Sshc {}>".format(self.id)

    @classmethod
    def add_many(cls, df: pd.DataFrame):
        data_dict: Dict[Any, Dict[str, Dict[str, float]]] = get_data(df)
        try:
            for time, data in data_dict.items():
                kwargs = {}
                for name in cls._mapping.keys():
                    try:
                        kwargs[name] = data[cls._mapping[name]]["_VALUE"]
                    except KeyError:
                        kwargs[name] = None

                obj = Sshc(time=time, qualified=data.get("qualified"), **kwargs)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise

    @classmethod
    def get_last_one(cls):
        obj: cls = cls.query.order_by(cls.id.desc()).first()
        return obj

    @classmethod
    def judge_limit(cls, df, limit: dict):
        # fields = ("sshc_cksf_up", "sshc_cksf_down")
        result = judge_limit(df, limit, "sshc_", cls._mapping)
        return result


class Yjl(Base, db.Model):
    """叶加料"""

    _mapping = {
        "wlsjll": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_PV_Massflow",
        "wlljzl": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_Total_Massflow",
        "ljjsl": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ST201_Total_Waterflow",
        "rksf": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF201_PV_Moisture",
        "ssjsl": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_03.OutPhyPV",
        "ssjll": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_04.OutPhyPV",
        "lywd": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.KA104_PV_ST201_Temperature",
        "ckwd": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Temp",
        "cksf": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Moisture",
    }
    __tablename__ = "yjl"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    time = db.Column(db.DateTime)  # 时间
    qualified = db.Column(db.Integer, default=0)  # 质量， 1 为符合， 0 为不符合

    wlsjll = db.Column(db.Float)  # 物料实际流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    ljjsl = db.Column(db.Float)  # 累计加水量
    rksf = db.Column(db.Float)  # 入口水分
    ssjsl = db.Column(db.Float)  # 瞬时加水量
    ssjll = db.Column(db.Float)  # 瞬时加料量
    lywd = db.Column(db.Float)  # 料液温度
    ckwd = db.Column(db.Float)  # 出口温度
    cksf = db.Column(db.Float)  # 出口水分

    wd = db.Column(db.Float)  # 温度
    sd = db.Column(db.Float)  # 湿度

    ycs = db.relationship("Yc", backref="yjl")  # 预测外键关系关联
    sssf_controls = db.relationship("SssfControl", backref="yjl")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Yjl {}>".format(self.id)

    @classmethod
    def get_last_one(cls):
        obj: cls = cls.query.order_by(cls.id.desc()).first()
        return obj

    @classmethod
    def add_many(cls, df):
        data_dict: Dict[Any, Dict[str, Dict[str, float]]] = get_data(df)

        try:
            for time, data in data_dict.items():
                kwargs = {}
                for name in cls._mapping.keys():
                    try:
                        kwargs[name] = data[cls._mapping[name]]["_VALUE"]
                    except KeyError:
                        kwargs[name] = None

                obj = Yjl(time=time, qualified=data.get("qualified"), **kwargs)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise

    @classmethod
    def get_last_one(cls):
        """
        返回最新的一个值
        """
        yjl: Yjl = Yjl.query.order_by(Yjl.id.desc()).first()
        return yjl

    @classmethod
    def judge_limit(cls, df, limit: dict):
        # fields = (
        #     "yjl_rksf_up",
        #     "yjl_rksf_down",
        #     "yjl_wlljzl_up",
        #     "yjl_wlljzl_down",
        #     "yjl_wlssll_up",
        #     "yjl_wlssll_down",
        #     "yjl_lywd_up",
        #     "yjl_lywd_down",
        #     "yjl_ljjsl_up",
        #     "yjl_ljjsl_down",
        #     "yjl_ssjsl_up",
        #     "yjl_ssjsl_down",
        #     "yjl_wd_up",
        #     "yjl_wd_down",
        #     "yjl_sd_up",
        #     "yjl_sd_down",
        #     "yjl_ckwd_up",
        #     "yjl_ckwd_down",
        #     "yjl_cksf_up",
        #     "yjl_cksf_down",
        # )
        result = judge_limit(df, limit, "yjl_", cls._mapping)
        return result


# 烘丝
class Hs(Base, db.Model):
    _mapping = {
        "sssf": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.MOIST_PV",
        "zqll": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamMaFl",
        "fhzqyl": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamPressAft",
        "fqzqyl": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamPressBef",
        "zqtj": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamVolFl",
        "y32fmz": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_ValPos_Y32",
        "wlsjll": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_PV",
        "wlljzl": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_TOT",
        "zqllfmkd": "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.CV_SteamMaFl",
    }
    __tablename__ = "hs"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    time = db.Column(db.DateTime)  # 时间
    qualified = db.Column(db.Integer, default=0)  # 质量， 1 为符合， 0 为不符合

    sssf = db.Column(db.Float)  # 生丝水分
    fhzqyl = db.Column(db.Float)  # 阀后蒸汽压力
    fqzqyl = db.Column(db.Float)  # 阀前蒸汽压力
    zqll = db.Column(db.Float)  # 蒸汽流量
    zqllfmkd = db.Column(db.Float)  # 蒸汽流量阀门开度
    zqtj = db.Column(db.Float)  # 蒸汽体积
    y32fmz = db.Column(db.Float)  # Y32阀门值
    wlsjll = db.Column(db.Float)  # 物料实际流量
    wlljzl = db.Column(db.Float)  # 物料累计重量

    ycs = db.relationship("Yc", backref="hs")  # 切丝外键关系关联

    sssf_controls = db.relationship("SssfControl", backref="hs")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Hs {}>".format(self.id)

    @classmethod
    def add_many(cls, df):
        data_dict: Dict[Any, Dict[str, Dict[str, float]]] = get_data(df)

        try:
            for time, data in data_dict.items():
                kwargs = {}
                for name in cls._mapping.keys():
                    try:
                        kwargs[name] = data[cls._mapping[name]]["_VALUE"]
                    except KeyError:
                        kwargs[name] = None

                obj = Hs(time=time, qualified=data.get("qualified"), **kwargs)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise

    @classmethod
    def get_last_one(cls):
        obj: cls = cls.query.order_by(cls.id.desc()).first()
        return obj

    @classmethod
    def judge_limit(cls, df, limit: dict):
        # fields = ("sssf_up", "sssf_down")
        result = judge_limit(df, limit, "", cls._mapping)
        return result


# 批次号分配器
class Pch(db.Model):
    __tablename__ = "pch"
    # sshc yjl hs
    name = db.Column(db.String(100), unique=True, primary_key=True)  # 名称
    value = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "<Pch {} {}>".format(self.name, self.value)

    @classmethod
    def get(cls, name):
        if name == "sshc":
            obj: SshcInfo = SshcInfo.query.order_by(SshcInfo.id.desc()).first()

        elif name == "yjl":
            obj: YjlInfo = YjlInfo.query.order_by(YjlInfo.id.desc()).first()

        elif name == "Hs":
            ...
            return

        item = cls.query.filter_by(name=name).first()
        return item.value if item else None

    @classmethod
    def set(cls, name, value):
        item = cls.query.filter_by(name=name).first()
        if item:
            cls.query.filter_by(name=name).update({Pch.value: value})
        else:
            obj = cls(name=name, value=value)
            db.session.add(obj)
        db.session.commit()


class Cy(Base, db.Model):
    """储叶"""

    __tablename__ = "cy"
    id = db.Column(db.Integer, primary_key=True)  # 编号

    wd = db.Column(db.Float)  # 温度
    sd = db.Column(db.Float)  # 湿度


class Qs(Base, db.Model):
    """储叶"""

    __tablename__ = "qs"
    id = db.Column(db.Integer, primary_key=True)  # 编号

    wd = db.Column(db.Float)  # 温度
    sd = db.Column(db.Float)  # 湿度


# 预测
class Yc(Base, db.Model):
    __tablename__ = "yc"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    yc_ljjsl = db.Column(db.Float)  # 预测的累积加水量
    yc_sssf = db.Column(db.Float)  # 预测的生丝水分值
    yc_sssfup = db.Column(db.Float)  # 预测的生丝水分上限
    yc_sssfdown = db.Column(db.Float)  # 预测的生丝水分下限

    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    hs_id = db.Column(db.Integer, db.ForeignKey("hs.id"))  # 烘丝

    def __repr__(self):
        return "<Yc {}>".format(self.id)
