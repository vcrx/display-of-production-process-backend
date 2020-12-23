from app import db
from .base import Base


# 生丝水分控制
class SssfControl(Base, db.Model):
    __tablename__ = "sssf_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号

    sshc_id = db.Column(db.Integer, db.ForeignKey("sshc.id"))  # 松散回潮
    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    hs_id = db.Column(db.Integer, db.ForeignKey("hs.id"))  # 叶加料
    bj_control_id = db.Column(db.Integer, db.ForeignKey("bj_control.id"))  # 报警控制
    rg_control_id = db.Column(db.Integer, db.ForeignKey("rg_control.id"))  # 人工控制

    def __repr__(self):
        return "<SssfControl {}>".format(self.id)


# 报警控制
class BjControl(Base, db.Model):
    # 存下历史所有的 BjControl，每次取最高 id 的一条就是了，相当于历史记录。
    __tablename__ = "bj_control"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 编号
    sshc_cksf_up = db.Column(db.Float)  # 松散回潮出口水分上限
    sshc_cksf_down = db.Column(db.Float)  # 松散回潮出口水分下限
    yjl_rksf_up = db.Column(db.Float)  # 叶加料入口水分上限
    yjl_rksf_down = db.Column(db.Float)  # 叶加料入口水分下限
    yjl_wlljzl_up = db.Column(db.Float)  # 叶加料物料累积重量上限
    yjl_wlljzl_down = db.Column(db.Float)  # 叶加料物料累积重量下限
    yjl_wlssll_up = db.Column(db.Float)  # 叶加料物料实时流量上限
    yjl_wlssll_down = db.Column(db.Float)  # 叶加料物料实时流量下限
    yjl_lywd_up = db.Column(db.Float)  # 叶加料料液温度上限
    yjl_lywd_down = db.Column(db.Float)  # 叶加料料液温度下限
    yjl_ljjsl_up = db.Column(db.Float)  # 叶加料累积加水量上限
    yjl_ljjsl_down = db.Column(db.Float)  # 叶加料累积加水量下限
    yjl_ssjsl_up = db.Column(db.Float)  # 叶加料瞬时加水量上限
    yjl_ssjsl_down = db.Column(db.Float)  # 叶加料瞬时加水量下限
    yjl_wd_up = db.Column(db.Float)  # 叶加料温度上限
    yjl_wd_down = db.Column(db.Float)  # 叶加料温度下限
    yjl_sd_up = db.Column(db.Float)  # 叶加料湿度上限
    yjl_sd_down = db.Column(db.Float)  # 叶加料湿度下限
    yjl_ckwd_up = db.Column(db.Float)  # 叶加料出口温度上限
    yjl_ckwd_down = db.Column(db.Float)  # 叶加料出口温度下限
    yjl_cksf_up = db.Column(db.Float)  # 叶加料出口水分上限
    yjl_cksf_down = db.Column(db.Float)  # 叶加料出口水分下限
    cy_wd_up = db.Column(db.Float)  # 储叶温度上限
    cy_wd_down = db.Column(db.Float)  # 储叶温度下限
    cy_sd_up = db.Column(db.Float)  # 储叶湿度上限
    cy_sd_down = db.Column(db.Float)  # 储叶湿度下限
    qs_wd_up = db.Column(db.Float)  # 切丝温度上限
    qs_wd_down = db.Column(db.Float)  # 切丝温度下限
    qs_sd_up = db.Column(db.Float)  # 切丝湿度上限
    qs_sd_down = db.Column(db.Float)  # 切丝湿度下限
    sssf_up = db.Column(db.Float)  # 生丝水分控制值上限
    sssf_down = db.Column(db.Float)  # 生丝水分控制值下限

    sssf_controls = db.relationship("SssfControl", backref="bj_control")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<BjControl {}>".format(self.id)

    @classmethod
    def get_last_one(cls):
        bj_control: cls = cls.query.order_by(cls.id.desc()).first()
        return bj_control


class BjRecords(Base, db.Model):
    """报警记录"""

    __tablename__ = "bj_records"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 编号
    time = db.Column(db.DateTime)  # 时间
    pph = db.Column(db.String(128))  # 品牌号
    pch = db.Column(db.Integer)  # 批次号
    stage = db.Column(db.String(128))  # 生产阶段
    factor = db.Column(db.String(128))  # 影响因素
    reason = db.Column(db.Text)  # 报警原因
    status = db.Column(db.Integer, default=0)  # 状态：未读0 已读1

    @classmethod
    def add_one(cls, dct: dict):
        """
        {
            datetime.datetime(2020, 10, 12, 13, 8, tzinfo=tzutc()): {
                'sshc_cksf_up': {'break': True, 'reason': 'sshc_cksf_up，范围：1.0 目前：18.630000115'},
                'sshc_cksf_down': {'break': True, 'reason': 'sshc_cksf_down，范围：9999.0 目前：18.630000115'}
            }
        }
        """
        for time, data in dct.items():
            for factor, v in data.items():
                obj = cls(
                    time=time,
                    pph="利群",
                    pch=None,
                    stage=factor,
                    factor=factor,
                    reason=v.get("reason"),
                )
                db.session.add(obj)
        db.session.commit()


# 人工控制
class RgControl(Base, db.Model):
    __tablename__ = "rg_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ljjsl = db.Column(db.Float)  # 人工计算的累积加水量
    sssf = db.Column(db.Float)  # 生丝水分目标值
    cysc = db.Column(db.DateTime)  # 储叶时长，这里存的是预计储叶结束时间
    sssf_controls = db.relationship("SssfControl", backref="rg_control")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<RgControl {}>".format(self.id)

    @classmethod
    def get_last_one(cls):
        obj: cls = cls.query.order_by(cls.id.desc()).first()
        return obj

    @classmethod
    def add_one(cls, **kwargs):
        obj = RgControl(**kwargs)
        db.session.add(obj)
        db.session.commit()
