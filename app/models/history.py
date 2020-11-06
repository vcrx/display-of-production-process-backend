from app import db
from .base import Base
from sqlalchemy import exc


# 松散回潮生产信息
class SshcInfo(Base, db.Model):
    __tablename__ = "sshc_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pch = db.Column(db.Integer)  # 批次号
    pph = db.Column(db.String(128))  # 品牌号
    rq = db.Column(db.DateTime)  # 日期
    wlssll = db.Column(db.Float)  # 物料实时流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    ljjsl = db.Column(db.Float)  # 累积加水量
    hfwd = db.Column(db.Float)  # 回风温度
    ckwd = db.Column(db.Float)  # 出口温度
    cksf = db.Column(db.Float)  # 出口水分
    
    def __repr__(self):
        return "<SshcInfo {}>".format(self.id)
    
    @classmethod
    def add_many(cls, datas):
        """
        datas: [{
            pch: "xxxx",
            ppj: "xxxx",
            ...
            cksf: "xxx"
        }, ...]
        datas 是一个包含 需要的字段数据的字典的 List[Dict[str, any]]
        """
        try:
            for data in datas:
                obj = SshcInfo(**data)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise


# 叶加料生产信息
class YjlInfo(Base, db.Model):
    __tablename__ = "yjl_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pch = db.Column(db.Integer)  # 批次号
    pph = db.Column(db.String(128))  # 品牌号
    rq = db.Column(db.DateTime)  # 日期
    rksf = db.Column(db.Float)  # 入口水分
    wlssll = db.Column(db.Float)  # 物料实时流量
    wlljzl = db.Column(db.Float)  # 物料累计重量
    cksf = db.Column(db.Float)  # 出口水分
    ckwd = db.Column(db.Float)  # 出口温度
    ljjsl = db.Column(db.Float)  # 累积加水量
    ly_ssll = db.Column(db.Float)  # 料液实时流量
    ly_ljjl = db.Column(db.Float)  # 料液流量累计加料量
    ly_wd = db.Column(db.Float)  # 料液温度
    
    def __repr__(self):
        return "<YjlInfo {}>".format(self.id)
    
    @classmethod
    def add_many(cls, datas):
        """
        datas: [{
            pch: "xxxx",
            ppj: "xxxx",
            ...
            cksf: "xxx"
        }, ...]
        datas 是一个包含 需要的字段数据的字典的 List[Dict[str, any]]
        """
        try:
            for data in datas:
                obj = YjlInfo(**data)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()


# 储叶生产信息
class CyInfo(Base, db.Model):
    __tablename__ = "cy_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pch = db.Column(db.Integer)  # 批次号
    pph = db.Column(db.String(128))  # 品牌号
    rq = db.Column(db.DateTime)  # 日期
    cysc = db.Column(db.Integer)  # 储叶时长
    wd = db.Column(db.Float)  # 储叶房温度
    sd = db.Column(db.Float)  # 储叶房湿度
    sssf = db.Column(db.Float)  # 生丝水分
    
    def __repr__(self):
        return "<CyInfo {}>".format(self.id)
    
    @classmethod
    def add_many(cls, datas):
        """
        datas: [{
            pch: "xxxx",
            ppj: "xxxx",
            ...
            cksf: "xxx"
        }, ...]
        datas 是一个包含 需要的字段数据的字典的 List[Dict[str, any]]
        """
        try:
            for data in datas:
                obj = CyInfo(**data)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise


# 切丝生产信息
class QsInfo(Base, db.Model):
    __tablename__ = "qs_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    pch = db.Column(db.Integer)  # 批次号
    pph = db.Column(db.String(128))  # 品牌号
    rq = db.Column(db.DateTime)  # 日期
    wd = db.Column(db.Float)  # 储丝房温度
    sd = db.Column(db.Float)  # 储丝房湿度
    
    def __repr__(self):
        return "<QsInfo {}>".format(self.id)
    
    @classmethod
    def add_many(cls, datas):
        """
        datas: [{
            pch: "xxxx",
            ppj: "xxxx",
            ...
            cksf: "xxx"
        }, ...]
        datas 是一个包含 需要的字段数据的字典的 List[Dict[str, any]]
        """
        try:
            for data in datas:
                obj = QsInfo(**data)
                db.session.add(obj)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise
