from datetime import datetime

from flask import session, request
from werkzeug.security import check_password_hash

from app import db
from .base import Base


# 角色
class Role(Base, db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 角色权限列表
    admins = db.relationship("Admin", backref="role")  # 管理员外键关系关联

    def __repr__(self):
        return "<Role {}>".format(self.name)


# 权限
class Auth(Base, db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址

    def __repr__(self):
        return "<Auth {}>".format(self.name)


# 管理员
class Admin(Base, db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(128))  # 管理员密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.Integer, unique=True)  # 电话号码
    is_super = db.Column(db.SmallInteger)  # 是否是超级管理员，0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))  # 所属角色
    adminlogs = db.relationship("AdminLoginLog", backref="admin")  # 管理员登录日志外键关联
    oplogs = db.relationship("Oplog", backref="admin")  # 管理员操作日志外键关联

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)

    def __repr__(self):
        return "<Admin {}>".format(self.name)


# 管理员登录日志
class AdminLoginLog(Base, db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ip = db.Column(db.String(100))  # 登录IP
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员

    def __repr__(self):
        return "<AdminLoginLog {}>".format(self.id)


# 操作日志
class Oplog(Base, db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(600))  # 操作原因
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员

    def __repr__(self):
        return "<Oplog {}>".format(self.id)

    @classmethod
    def add_one(cls, reason="unknow op"):
        oplog = Oplog(
            admin_id=session["admin_id"], ip=request.remote_addr, reason=reason
        )
        db.session.add(oplog)
        db.session.commit()
