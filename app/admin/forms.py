from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    SelectMultipleField,
)
from wtforms.validators import EqualTo, DataRequired, ValidationError
from app.models import Admin, Auth, Role

auth_list = Auth.query.all()
role_list = Role.query.all()


#   管理员登录表单
class LoginForm(FlaskForm):
    account = StringField(
        label="账号",
        validators=[DataRequired("请输入账号！")],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号",
            # "required": "required"      # 必填项
        },
    )

    pwd = PasswordField(
        label="密码",
        validators=[DataRequired("请输入密码！")],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
            # "required": "required"
        },
    )

    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        },
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在!")


# 密码表单
class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("请输入旧密码..."),
        ],
        description="旧密码",
        render_kw={"class": "form-control", "placeholder": "请输入旧密码！"},
    )

    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("请输入新密码..."),
        ],
        description="新密码",
        render_kw={"class": "form-control", "placeholder": "请输入新密码！"},
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary",
        },
    )

    def validate_old_pwd(self, field):
        from flask import session

        pwd = field.data
        name = session["admin"]
        admin = Admin.query.filter_by(name=name).first()
        if not admin.check_pwd(pwd):
            raise ValidationError("旧密码输入错误!")


# 权限管理表单
class AuthForm(FlaskForm):
    name = StringField(
        label="权限",
        validators=[
            DataRequired("请输入权限!"),
        ],
        description="权限",
        render_kw={"class": "form-control", "placeholder": "请输入权限！"},
    )

    url = StringField(
        label="权限地址",
        validators=[
            DataRequired("请输入权限地址!"),
        ],
        description="权限地址",
        render_kw={"class": "form-control", "placeholder": "请输入权限地址！"},
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary",
        },
    )


# 角色管理表单
class RoleForm(FlaskForm):
    name = StringField(
        label="角色名称",
        validators=[
            DataRequired("请输入角色名称!"),
        ],
        description="角色名称",
        render_kw={"class": "form-control", "placeholder": "请输入角色名称！"},
    )

    auths = SelectMultipleField(
        label="权限列表",
        validators=[
            DataRequired("请选择权限!"),
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in auth_list],
        description="权限列表",
        render_kw={
            "class": "form-control",
        },
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary",
        },
    )


# 管理员表单
class AdminForm(FlaskForm):
    name = StringField(
        label="管理员名称",
        validators=[
            DataRequired("请输入管理员名称!"),
        ],
        description="管理员名称",
        render_kw={"class": "form-control", "placeholder": "请输入管理员名称！"},
    )

    pwd = PasswordField(
        label="管理员密码",
        validators=[DataRequired("请输入管理员密码!")],
        description="管理员密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员密码！",
            "required": "required",
        },
    )

    repwd = PasswordField(
        label="管理员重复密码",
        validators=[
            DataRequired("请输入管理员重复密码!"),
            EqualTo("pwd", message="两次密码不一致!"),
        ],
        description="管理员重复密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员重复密码！",
            "required": "required",
        },
    )

    role_id = SelectField(
        label="所属角色",
        validators=[DataRequired("请选择角色!")],
        coerce=int,
        choices=[(v.id, v.name) for v in role_list],
        description="所属角色",
        render_kw={
            "class": "form-control",
        },
    )

    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary",
        },
    )
