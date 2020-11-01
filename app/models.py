# type: ignore
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


# 松散回潮
class Sshc(db.Model):
    __tablename__ = "sshc"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    sshc_rksf = db.Column(db.Integer)  # 入口水分
    sshc_wd = db.Column(db.Integer)  # 温度
    sshc_sd = db.Column(db.Integer)  # 湿度
    sshc_cksf = db.Column(db.Integer)  # 出口水分
    sssf_controls = db.relationship("Sssf_control", backref="sshc")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Sshc {}>".format(self.id)


# 叶加料
class Yjl(db.Model):
    __tablename__ = "yjl"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    yjl_rksf = db.Column(db.Integer)  # 入口水分
    yjl_cljzl = db.Column(db.Integer)  # 物料累积重量
    yjl_cssll = db.Column(db.Integer)  # 物料瞬时流量
    yjl_lywd = db.Column(db.Integer)  # 料液温度
    yjl_ljjsl = db.Column(db.Integer)  # 实时累积加水量
    yjl_ssjsl = db.Column(db.Integer)  # 瞬时加水量
    yjl_wd = db.Column(db.Integer)  # 温度
    yjl_sd = db.Column(db.Integer)  # 湿度
    yjl_ckwd = db.Column(db.Integer)  # 出口温度
    yjl_cksf = db.Column(db.Integer)  # 出口水分
    yjlsc = db.Column(db.Integer)  # 叶加料时长

    kshs = db.relationship("Ksh", backref="yjl")  # 可视化外键关系关联
    ycs = db.relationship("Yc", backref="yjl")  # 预测外键关系关联
    sssf_controls = db.relationship("Sssf_control", backref="yjl")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Yjl {}>".format(self.id)


# 储叶
class Cy(db.Model):
    __tablename__ = "cy"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    cy_wd = db.Column(db.Integer)  # 温度
    cy_sd = db.Column(db.Integer)  # 湿度
    cysc = db.Column(db.Integer)  # 储叶时长

    kshs = db.relationship("Ksh", backref="cy")  # 可视化外键关系关联
    ycs = db.relationship("Yc", backref="cy")  # 预测外键关系关联
    sssf_controls = db.relationship("Sssf_control", backref="cy")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Cy {}>".format(self.id)


# 切丝
class Qs(db.Model):
    __tablename__ = "qs"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    qs_wd = db.Column(db.Integer)  # 温度
    qs_sd = db.Column(db.Integer)  # 湿度
    qssc = db.Column(db.Integer)  # 切丝时长

    kshs = db.relationship("Ksh", backref="qs")  # 可视化外键关系关联
    ycs = db.relationship("Yc", backref="qs")  # 切丝外键关系关联
    sssf_controls = db.relationship("Sssf_control", backref="qs")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Qs {}>".format(self.id)


# 生丝水分
class Sssf(db.Model):
    __tablename__ = "sssf"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    sssf_mean = db.Column(db.Integer)  # 均值
    sssf_bp = db.Column(db.Integer)  # 标偏
    sssf_hgl = db.Column(db.Integer)  # 合格率
    sssf_cpk = db.Column(db.Integer)  # CPK

    sssf_controls = db.relationship("Sssf_control", backref="sssf")  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Sssf {}>".format(self.id)


# 报警控制
class Bj_control(db.Model):
    __tablename__ = "bj_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    sshc_cksfup = db.Column(db.Integer)  # 松散回潮出口水分上限
    sshc_cksfdown = db.Column(db.Integer)  # 松散回潮出口水分下限
    yjl_rksfup = db.Column(db.Integer)  # 叶加料入口水分上限
    yjl_rksfdown = db.Column(db.Integer)  # 叶加料入口水分下限
    yjl_cljzlup = db.Column(db.Integer)  # 叶加料秤累积重量上限
    yjl_cljzldown = db.Column(db.Integer)  # 叶加料秤累积重量下限
    yjl_cssllup = db.Column(db.Integer)  # 叶加料秤瞬时流量上限
    yjl_csslldown = db.Column(db.Integer)  # 叶加料秤瞬时流量下限
    yjl_lywdup = db.Column(db.Integer)  # 叶加料料液温度上限
    yjl_lywddown = db.Column(db.Integer)  # 叶加料料液温度下限
    yjl_ljjslup = db.Column(db.Integer)  # 叶加料累积加水量上限
    yjl_ljjsldown = db.Column(db.Integer)  # 叶加料累积加水量下限
    yjl_ssjslup = db.Column(db.Integer)  # 叶加料瞬时加水量上限
    yjl_ssjsldown = db.Column(db.Integer)  # 叶加料瞬时加水量下限
    yjl_wdup = db.Column(db.Integer)  # 叶加料温度上限
    yjl_wddown = db.Column(db.Integer)  # 叶加料温度下限
    yjl_sdup = db.Column(db.Integer)  # 叶加料湿度上限
    yjl_sddown = db.Column(db.Integer)  # 叶加料湿度下限
    yjl_ckwdup = db.Column(db.Integer)  # 叶加料出口温度上限
    yjl_ckwddown = db.Column(db.Integer)  # 叶加料出口温度下限
    yjl_cksfup = db.Column(db.Integer)  # 叶加料出口水分上限
    yjl_cksfdown = db.Column(db.Integer)  # 叶加料出口水分下限
    cy_wdup = db.Column(db.Integer)  # 储叶温度上限
    cy_wddown = db.Column(db.Integer)  # 储叶温度下限
    cy_sdup = db.Column(db.Integer)  # 储叶湿度上限
    cy_sddown = db.Column(db.Integer)  # 储叶湿度下限
    qs_wdup = db.Column(db.Integer)  # 切丝温度上限
    qs_wddown = db.Column(db.Integer)  # 切丝温度下限
    qs_sdup = db.Column(db.Integer)  # 切丝湿度上限
    qs_sddown = db.Column(db.Integer)  # 切丝湿度下限

    sssf_controls = db.relationship(
        "Sssf_control", backref="bj_control"
    )  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Bj_control {}>".format(self.id)


# 人工控制
class Rg_control(db.Model):
    __tablename__ = "rg_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    rg_ljjsl = db.Column(db.Integer)  # 人工计算的累积加水量

    sssf_controls = db.relationship(
        "Sssf_control", backref="rg_control"
    )  # 生丝水分控制外键关系关联

    def __repr__(self):
        return "<Rg_control {}>".format(self.id)


# 生丝水分控制
class Sssf_control(db.Model):
    __tablename__ = "sssf_control"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ycy_time = db.Column(db.Integer)  # 预储叶时间

    sshc_id = db.Column(db.Integer, db.ForeignKey("sshc.id"))  # 松散回潮
    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    cy_id = db.Column(db.Integer, db.ForeignKey("cy.id"))  # 储叶
    qs_id = db.Column(db.Integer, db.ForeignKey("qs.id"))  # 切丝
    sssf_id = db.Column(db.Integer, db.ForeignKey("sssf.id"))  # 生丝水分
    bj_control_id = db.Column(db.Integer, db.ForeignKey("bj_control.id"))  # 报警控制
    rg_control_id = db.Column(db.Integer, db.ForeignKey("rg_control.id"))  # 人工控制

    def __repr__(self):
        return "<Sssf_control {}>".format(self.id)


# 预测
class Yc(db.Model):
    __tablename__ = "yc"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    yc_ljjsl = db.Column(db.Integer)  # 预测的累积加水量
    yc_sssf = db.Column(db.Integer)  # 预测的生丝水分值
    yc_sssfup = db.Column(db.Integer)  # 预测的生丝水分上限
    yc_sssfdown = db.Column(db.Integer)  # 预测的生丝水分下限

    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    cy_id = db.Column(db.Integer, db.ForeignKey("cy.id"))  # 储叶
    qs_id = db.Column(db.Integer, db.ForeignKey("qs.id"))  # 切丝

    def __repr__(self):
        return "<Yc {}>".format(self.id)


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    auths = db.Column(db.String(600))  # 角色权限列表

    admins = db.relationship("Admin", backref="role")  # 管理员外键关系关联

    def __repr__(self):
        return "<Role {}>".format(self.name)


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Auth {}>".format(self.name)


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(128))  # 管理员密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.Integer, unique=True)  # 电话号码
    is_super = db.Column(db.SmallInteger)  # 是否是超级管理员，0为超级管理员
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))  # 所属角色

    adminlogs = db.relationship("Adminloginlog", backref="admin")  # 管理员登录日志外键关联
    oplogs = db.relationship("Oplog", backref="admin")  # 管理员操作日志外键关联

    # def get_pwd(self):
    #     return self.pwd

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)

    def __repr__(self):
        return "<Admin {}>".format(self.name)


# 管理员登录日志
class Adminloginlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员

    def __repr__(self):
        return "<Adminloginlog {}>".format(self.id)


# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员

    def __repr__(self):
        return "<Oplog {}>".format(self.id)


# 可视化
class Ksh(db.Model):
    __tablename__ = "ksh"
    id = db.Column(db.Integer, primary_key=True)  # 编号

    yjl_id = db.Column(db.Integer, db.ForeignKey("yjl.id"))  # 叶加料
    cy_id = db.Column(db.Integer, db.ForeignKey("cy.id"))  # 储叶
    qs_id = db.Column(db.Integer, db.ForeignKey("qs.id"))  # 切丝

    def __repr__(self):
        return "<Ksh {}>".format(self.id)


# 松散回潮生产信息
class Sshc_info(db.Model):
    __tablename__ = "sshc_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    sshc_rksf = db.Column(db.Integer)  # 入口水分
    sshc_wd = db.Column(db.Integer)  # 温度
    sshc_sd = db.Column(db.Integer)  # 湿度
    sshc_ljjsl = db.Column(db.Integer)  # 累积加水量
    sshc_cksf = db.Column(db.Integer)  # 出口水分

    tjcxs = db.relationship("Tjcx", backref="sshc_info")  # 统计查询外键关联

    def __repr__(self):
        return "<Sshc_info {}>".format(self.id)


# 叶加料生产信息
class Yjl_info(db.Model):
    __tablename__ = "yjl_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ykl_bch = db.Column(db.Integer)  # 班次号
    ykl_pch = db.Column(db.Integer)  # 批次号
    ykl_pph = db.Column(db.Integer)  # 品牌号
    ykl_czh = db.Column(db.Integer)  # 操作号
    ykl_pfh = db.Column(db.Integer)  # 配方号
    ykl_mkh = db.Column(db.Integer)  # 模块号
    ykl_product_start_time = db.Column(
        db.DateTime, index=True, default=datetime.now
    )  # 生产开始时间
    ykl_product_end_time = db.Column(
        db.DateTime, index=True, default=datetime.now
    )  # 生产结束时间
    ykl_zqyl = db.Column(db.Integer)  # 蒸汽压力
    ykl_yskqyl = db.Column(db.Integer)  # 压缩空气压力
    ykl_syl = db.Column(db.Integer)  # 水压力
    ykl_rksf = db.Column(db.Integer)  # 入口水分
    ykl_pckd = db.Column(db.Integer)  # 排潮开度
    ykl_pcfl = db.Column(db.Integer)  # 排潮风量
    ykl_rffl = db.Column(db.Integer)  # 热风风量
    ykl_bczqfmkd = db.Column(db.Integer)  # 补偿蒸汽阀门开度
    ykl_jyfhzqyl = db.Column(db.Integer)  # 减压阀后蒸汽压力
    ykl_lywd = db.Column(db.Integer)  # 料液温度
    ykl_jlbsssd = db.Column(db.Integer)  # 加料泵实时速度

    tjcxs = db.relationship("Tjcx", backref="yjl_info")  # 统计查询外键关联

    def __repr__(self):
        return "<Yjl_info {}>".format(self.id)


# 储叶生产信息
class Cy_info(db.Model):
    __tablename__ = "cy_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    cy_bch = db.Column(db.Integer)  # 班次号
    cy_pch = db.Column(db.Integer)  # 批次号
    cy_pph = db.Column(db.Integer)  # 品牌号
    cy_czh = db.Column(db.Integer)  # 操作号
    cy_pfh = db.Column(db.Integer)  # 配方号
    cy_mkh = db.Column(db.Integer)  # 模块号
    cy_product_start_time = db.Column(
        db.DateTime, index=True, default=datetime.now
    )  # 生产开始时间
    cy_product_end_time = db.Column(
        db.DateTime, index=True, default=datetime.now
    )  # 生产结束时间
    cysc = db.Column(db.Integer)  # 储叶时长

    tjcxs = db.relationship("Tjcx", backref="cy_info")  # 统计查询外键关联

    def __repr__(self):
        return "<Cy_info {}>".format(self.id)


# 切丝生产信息
class Qs_info(db.Model):
    __tablename__ = "qs_info"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    qs_bch = db.Column(db.Integer)  # 班次号
    qs_pch = db.Column(db.Integer)  # 批次号
    qs_pph = db.Column(db.Integer)  # 品牌号
    qs_czh = db.Column(db.Integer)  # 操作号
    qs_pfh = db.Column(db.Integer)  # 配方号
    qs_mkh = db.Column(db.Integer)  # 模块号
    qs_product_start_time = db.Column(
        db.DateTime, index=True, default=datetime.now
    )  # 生产开始时间
    qs_product_end_time = db.Column(
        db.DateTime, index=True, default=datetime.now
    )  # 生产结束时间
    qs_zqyl = db.Column(db.Integer)  # 蒸汽压力
    qs_yskqyl = db.Column(db.Integer)  # 压缩空气压力
    qs_syl = db.Column(db.Integer)  # 水压力
    qs_rfwd = db.Column(db.Integer)  # 热风温度

    tjcxs = db.relationship("Tjcx", backref="qs_info")  # 统计查询外键关联

    def __repr__(self):
        return "<Qs_info {}>".format(self.id)


# 统计查询
class Tjcx(db.Model):
    __tablename__ = "tjcx"
    id = db.Column(db.Integer, primary_key=True)  # 编号

    sshc_info_id = db.Column(db.Integer, db.ForeignKey("sshc_info.id"))  # 松散回潮生产信息
    yjl_info_id = db.Column(db.Integer, db.ForeignKey("yjl_info.id"))  # 叶加料生产信息
    cy_info_id = db.Column(db.Integer, db.ForeignKey("cy_info.id"))  # 储叶生产信息
    qs_info_id = db.Column(db.Integer, db.ForeignKey("qs_info.id"))  # 切丝生产信息

    def __repr__(self):
        return "<Tjcx {}>".format(self.id)
