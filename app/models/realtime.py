from app import db
from typing import Dict
from .base import Base
from sqlalchemy import exc


# 松散回潮
class Sshc(Base, db.Model):
    __tablename__ = "sshc"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    time = db.Column(db.String(20))  # 时间
    wlssll = db.Column(db.Float)  # 物料实时流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    hfwd = db.Column(db.Float)  # 回风温度
    ckwd = db.Column(db.Float)  # 出口温度
    cksf = db.Column(db.Float)  # 出口水分
    sssf_controls = db.relationship("SssfControl",
                                    backref="sshc")  # 生丝水分控制外键关系关联
    
    def __repr__(self):
        return "<Sshc {}>".format(self.id)
    
    @classmethod
    def add_many(cls, data_dict: Dict[str, Dict[str, Dict[str, float]]]):
        map = {
            "wlssll": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_PV_Massflow",
            "wlljzl": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_Total_Massflow",
            "hfwd": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.TB101_PV_Temperature",
            "cksf": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Moisture",
            "ckwd": "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Temp",
        }
        try:
            for time, data in data_dict.items():
                kwargs = {}
                for name in map.keys():
                    try:
                        kwargs[name] = data[map[name]]["_VALUE"]
                    except KeyError:
                        kwargs[name] = None
                obj = Sshc(time=time, **kwargs)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise


# 叶加料
class Yjl(Base, db.Model):
    __tablename__ = "yjl"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    time = db.Column(db.String(20))  # 时间
    
    wlsjll = db.Column(db.Float)  # 物料实际流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    ljjsl = db.Column(db.Float)  # 累计加水量
    rksf = db.Column(db.Float)  # 入口水分
    ssjsl = db.Column(db.Float)  # 瞬时加水量
    ssjlj = db.Column(db.Float)  # 瞬时加料量
    lywd = db.Column(db.Float)  # 料液温度
    ckwd = db.Column(db.Float)  # 出口温度
    cksf = db.Column(db.Float)  # 出口水分
    
    kshs = db.relationship("Ksh", backref="yjl")  # 可视化外键关系关联
    ycs = db.relationship("Yc", backref="yjl")  # 预测外键关系关联
    sssf_controls = db.relationship("SssfControl",
                                    backref="yjl")  # 生丝水分控制外键关系关联
    
    def __repr__(self):
        return "<Yjl {}>".format(self.id)
    
    @classmethod
    def add_many(cls, data_dict):
        map = {
            "wlsjll": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_PV_Massflow",
            "wlljzl": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_Total_Massflow",
            "ljjsl": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ST201_Total_Waterflow",
            "rksf": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF201_PV_Moisture",
            "ssjsl": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_03.OutPhyPV",
            "ssjlj": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_04.OutPhyPV",
            "lywd": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.KA104_PV_ST201_Temperature",
            "ckwd": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Temp",
            "cksf": "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Moisture",
        }
        try:
            for time, data in data_dict.items():
                kwargs = {}
                for name in map.keys():
                    try:
                        kwargs[name] = data[map[name]]["_VALUE"]
                    except KeyError:
                        kwargs[name] = None
                obj = Yjl(time=time, **kwargs)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise


# 烘丝
class Hs(Base, db.Model):
    __tablename__ = "hs"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    time = db.Column(db.String(20))  # 时间
    
    sssf = db.Column(db.Float)  # 生丝水分
    fhzqyl = db.Column(db.Float)  # 阀后蒸汽压力
    fqzqyl = db.Column(db.Float)  # 阀前蒸汽压力
    zqll = db.Column(db.Float)  # 蒸汽流量
    zqllfmkd = db.Column(db.Float)  # 蒸汽流量阀门开度
    zqtj = db.Column(db.Float)  # 蒸汽体积
    y32fmz = db.Column(db.Float)  # Y32阀门值
    wlsjll = db.Column(db.Float)  # 物料实际流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    
    kshs = db.relationship("Ksh", backref="hs")  # 可视化外键关系关联
    ycs = db.relationship("Yc", backref="hs")  # 切丝外键关系关联
    
    sssf_controls = db.relationship("SssfControl", backref="hs")  # 生丝水分控制外键关系关联
    
    def __repr__(self):
        return "<Hs {}>".format(self.id)
    
    @classmethod
    def add_many(cls, data_dict):
        map = {
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
        try:
            for time, data in data_dict.items():
                kwargs = {}
                for name in map.keys():
                    try:
                        kwargs[name] = data[map[name]]["_VALUE"]
                    except KeyError:
                        kwargs[name] = None
                obj = Hs(time=time, **kwargs)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise


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


# 可视化
class Ksh(Base, db.Model):
    __tablename__ = "ksh"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    
    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    hs_id = db.Column(db.Integer, db.ForeignKey("hs.id"))  # 烘丝
    
    def __repr__(self):
        return "<Ksh {}>".format(self.id)
