from app import db
from datetime import datetime


# 松散回潮生产信息
class SshcInfo(db.Model):
    __tablename__ = "sshc_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ssll = db.Column(db.Float)  # 实时流量
    ljzl = db.Column(db.Float)  # 累计重量
    ljjsl = db.Column(db.Float)  # 累积加水量
    hfwd = db.Column(db.Float)  # 回风温度
    ckwd = db.Column(db.Float)  # 出口温度
    cksf = db.Column(db.Float)  # 出口水分
    tjcxs = db.relationship("Tjcx", backref="sshc_info")  # 统计查询外键关联
    
    def __repr__(self):
        return "<SshcInfo {}>".format(self.id)


# 叶加料生产信息
class YjlInfo(db.Model):
    __tablename__ = "yjl_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号

    rksf = db.Column(db.Float)  # 入口水分
    wlssll = db.Column(db.Float)  # 物料实时流量
    ljzl = db.Column(db.Float)  # 累计重量
    cksf = db.Column(db.Float)  # 出口水分
    ckwd = db.Column(db.Float)  # 出口温度
    ljjsl = db.Column(db.Float)  # 累积加水量
    ly_sjll = db.Column(db.Float)  # 料液实时流量
    ly_ljjl = db.Column(db.Float)  # 料液流量累计加料量
    ly_wd = db.Column(db.Float)  # 料液温度

    tjcxs = db.relationship("Tjcx", backref="yjl_info")  # 统计查询外键关联
    
    def __repr__(self):
        return "<YjlInfo {}>".format(self.id)


# 储叶生产信息
class CyInfo(db.Model):
    __tablename__ = "cy_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    cysc = db.Column(db.Integer)  # 储叶时长
    tjcxs = db.relationship("Tjcx", backref="cy_info")  # 统计查询外键关联
    
    def __repr__(self):
        return "<CyInfo {}>".format(self.id)


# 切丝生产信息
class QsInfo(db.Model):
    __tablename__ = "qs_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    
    rksf = db.Column(db.Float)  # 入口水分
    zqbmfkd = db.Column(db.Float)  # 蒸汽薄膜阀开度
    zqyl = db.Column(db.Float)  # 蒸汽压力
    zqzlll = db.Column(db.Float)  # 蒸汽质量流量
    zqtjll = db.Column(db.Float)  # 蒸汽体积流量
    zqjyfhyl = db.Column(db.Float)  # 蒸汽减压阀后压力
    ckwd = db.Column(db.Float)  # 出口温度
    
    yskqyl = db.Column(db.Float)  # 压缩空气压力
    syl = db.Column(db.Float)  # 水压力
    rfwd = db.Column(db.Float)  # 热风温度

    tjcxs = db.relationship("Tjcx", backref="qs_info")  # 统计查询外键关联
    
    def __repr__(self):
        return "<QsInfo {}>".format(self.id)


# 统计查询
class Tjcx(db.Model):
    __tablename__ = "tjcx"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pch = db.Column(db.Integer)  # 批次号
    pph = db.Column(db.String(128))  # 品牌号

    sshc_info_id = db.Column(db.Integer,
                             db.ForeignKey("sshc_info.id"))  # 松散回潮生产信息
    yjl_info_id = db.Column(db.Integer, db.ForeignKey("yjl_info.id"))  # 叶加料生产信息
    cy_info_id = db.Column(db.Integer, db.ForeignKey("cy_info.id"))  # 储叶生产信息
    qs_info_id = db.Column(db.Integer, db.ForeignKey("qs_info.id"))  # 切丝生产信息
    
    def __repr__(self):
        return "<Tjcx {}>".format(self.id)
