from app import db
from .base import Base


# 生丝水分控制
class SssfControl(Base, db.Model):
    __tablename__ = "sssf_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    target_value = db.Column(db.Float)  # 目标值
    
    sshc_id = db.Column(db.Integer, db.ForeignKey("sshc.id"))  # 松散回潮
    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    hs_id = db.Column(db.Integer, db.ForeignKey("hs.id"))  # 叶加料
    bj_control_id = db.Column(db.Integer,
                              db.ForeignKey("bj_control.id"))  # 报警控制
    rg_control_id = db.Column(db.Integer,
                              db.ForeignKey("rg_control.id"))  # 人工控制
    
    def __repr__(self):
        return "<SssfControl {}>".format(self.id)


# 报警控制
class BjControl(Base, db.Model):
    # 存下历史所有的 BjControl，每次取最高 id 的一条就是了，相当于历史记录。
    __tablename__ = "bj_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    sshc_cksfup = db.Column(db.Float)  # 松散回潮出口水分上限
    sshc_cksfdown = db.Column(db.Float)  # 松散回潮出口水分下限
    yjl_rksfup = db.Column(db.Float)  # 叶加料入口水分上限
    yjl_rksfdown = db.Column(db.Float)  # 叶加料入口水分下限
    yjl_cljzlup = db.Column(db.Float)  # 叶加料秤累积重量上限
    yjl_cljzldown = db.Column(db.Float)  # 叶加料秤累积重量下限
    yjl_cssllup = db.Column(db.Float)  # 叶加料秤瞬时流量上限
    yjl_csslldown = db.Column(db.Float)  # 叶加料秤瞬时流量下限
    yjl_lywdup = db.Column(db.Float)  # 叶加料料液温度上限
    yjl_lywddown = db.Column(db.Float)  # 叶加料料液温度下限
    yjl_ljjslup = db.Column(db.Float)  # 叶加料累积加水量上限
    yjl_ljjsldown = db.Column(db.Float)  # 叶加料累积加水量下限
    yjl_ssjslup = db.Column(db.Float)  # 叶加料瞬时加水量上限
    yjl_ssjsldown = db.Column(db.Float)  # 叶加料瞬时加水量下限
    yjl_wdup = db.Column(db.Float)  # 叶加料温度上限
    yjl_wddown = db.Column(db.Float)  # 叶加料温度下限
    yjl_sdup = db.Column(db.Float)  # 叶加料湿度上限
    yjl_sddown = db.Column(db.Float)  # 叶加料湿度下限
    yjl_ckwdup = db.Column(db.Float)  # 叶加料出口温度上限
    yjl_ckwddown = db.Column(db.Float)  # 叶加料出口温度下限
    yjl_cksfup = db.Column(db.Float)  # 叶加料出口水分上限
    yjl_cksfdown = db.Column(db.Float)  # 叶加料出口水分下限
    cy_wdup = db.Column(db.Float)  # 储叶温度上限
    cy_wddown = db.Column(db.Float)  # 储叶温度下限
    cy_sdup = db.Column(db.Float)  # 储叶湿度上限
    cy_sddown = db.Column(db.Float)  # 储叶湿度下限
    qs_wdup = db.Column(db.Float)  # 切丝温度上限
    qs_wddown = db.Column(db.Float)  # 切丝温度下限
    qs_sdup = db.Column(db.Float)  # 切丝湿度上限
    qs_sddown = db.Column(db.Float)  # 切丝湿度下限
    
    sssf_controls = db.relationship(
        "SssfControl", backref="bj_control"
    )  # 生丝水分控制外键关系关联
    
    def __repr__(self):
        return "<BjControl {}>".format(self.id)
    
    @classmethod
    def get_last_one(cls):
        bj_control: BjControl = BjControl.query.order_by(
            BjControl.id.desc()).first()
        return bj_control


# 人工控制
class RgControl(Base, db.Model):
    __tablename__ = "rg_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    rg_ljjsl = db.Column(db.Float)  # 人工计算的累积加水量
    
    sssf_controls = db.relationship(
        "SssfControl", backref="rg_control"
    )  # 生丝水分控制外键关系关联
    
    def __repr__(self):
        return "<RgControl {}>".format(self.id)
