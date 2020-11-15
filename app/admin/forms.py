import math

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    SelectMultipleField,
    FloatField
)
from wtforms.validators import (
    EqualTo,
    DataRequired,
    ValidationError,
    Optional,
)

from app.models.admin import Admin, Auth, Role


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
    
    def __init__(self):
        super().__init__()
        auth_list = Auth.query.all()
        self.auths.choices = [(v.id, v.name) for v in auth_list]


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
    
    def __init__(self):
        super().__init__()
        role_list = Role.query.all()
        self.role_id.choices = [(v.id, v.name) for v in role_list]


class NumberRange(object):
    """
    Validates that a number is of a minimum and/or maximum value, inclusive.
    This will work with any comparable number type, such as floats and
    decimals, not just integers.

    :param min:
        The minimum required value of the number. If not provided, minimum
        value will not be checked.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated using `%(min)s` and `%(max)s` if desired. Useful defaults
        are provided depending on the existence of min and max.
    """
    
    def __init__(self, min=None, message=None):
        self.min = min
        self.message = message
    
    def __call__(self, form, field):
        data = field.data
        if data is None:
            return
        if (math.isnan(data)) or \
                (self.min is not None and data < self.min):
            message = self.message
            raise ValidationError(message % dict(min=self.min))


class AlarmField(FloatField):
    def __init__(self, label, require_min=0.0, **kwargs):
        validates = [Optional()]
        if require_min is not None:
            validates.append(
                NumberRange(min=require_min, message=label + "不得小于 %(min)s"))
        super(AlarmField, self).__init__(
            label,
            validates,
            **kwargs
        )
    
    def gettext(self, _):
        return "不是有效的浮点数"


class AlarmForm(FlaskForm):
    sshc_cksfup = AlarmField("松散回潮出口水分上限")
    sshc_cksfdown = AlarmField("松散回潮出口水分下限")
    yjl_rksfup = AlarmField("叶加料入口水分上限")
    yjl_rksfdown = AlarmField("叶加料入口水分下限")
    yjl_wlljzlup = AlarmField("叶加料物料累积重量")
    yjl_wlljzldown = AlarmField("叶加料物料累积重量下限")
    yjl_wlssllup = AlarmField("叶加料物料实时流量上限")
    yjl_wlsslldown = AlarmField("叶加料物料实时流量下限")
    yjl_lywdup = AlarmField("叶加料料液温度上限")
    yjl_lywddown = AlarmField("叶加料料液温度下限")
    yjl_ljjslup = AlarmField("叶加料累积加水量上限")
    yjl_ljjsldown = AlarmField("叶加料累积加水量下限")
    yjl_ssjslup = AlarmField("叶加料瞬时加水量上限")
    yjl_ssjsldown = AlarmField("叶加料瞬时加水量下限")
    yjl_wdup = AlarmField("叶加料温度上限")
    yjl_wddown = AlarmField("叶加料温度下限")
    yjl_sdup = AlarmField("叶加料湿度上限")
    yjl_sddown = AlarmField("叶加料湿度下限")
    yjl_ckwdup = AlarmField("叶加料出口温度上限")
    yjl_ckwddown = AlarmField("叶加料出口温度下限")
    yjl_cksfup = AlarmField("叶加料出口水分上限")
    yjl_cksfdown = AlarmField("叶加料出口水分下限")
    cy_wdup = AlarmField("储叶温度上限")
    cy_wddown = AlarmField("储叶温度下限")
    cy_sdup = AlarmField("储叶湿度上限")
    cy_sddown = AlarmField("储叶湿度下限")
    qs_wdup = AlarmField("切丝温度上限")
    qs_wddown = AlarmField("切丝温度下限")
    qs_sdup = AlarmField("切丝湿度上限")
    qs_sddown = AlarmField("切丝湿度下限")
    sssf_up = AlarmField("生丝水分控制值上限", require_min=None)
    sssf_down = AlarmField("生丝水分控制值下限", require_min=None)
    
    def __init__(self):
        super(AlarmForm, self).__init__()
