from . import admin
from flask import render_template, redirect, url_for, flash, session, request, \
    abort
from app.admin.forms import LoginForm, PwdForm, AuthForm, RoleForm, AdminForm
from app.models import Admin, Auth, Role, AdminLoginLog, Oplog, BjControl
from functools import wraps
from app import db
import datetime


# 上下文应用处理器
@admin.context_processor
def tpl_extra():
    data = dict(
        online_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return data


# 登录请求验证
def admin_login_req(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return func(*args, **kwargs)
    
    return decorated_function


# 访问权限控制
def admin_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        admin = (
            Admin.query.join(Role)
                .filter(Role.id == Admin.role_id,
                        Admin.id == session["admin_id"])
                .first()
        )
        auths = admin.role.auths
        auths = list(map(lambda x: int(x), auths.split(",")))
        auth_list = Auth.query.all()
        urls = [v.url for v in auth_list for val in auths if val == v.id]
        rule = request.url_rule
        if str(rule) not in urls:
            abort(404)
        return func(*args, **kwargs)
    
    return decorated_function


"""----------视图函数----------"""


# @admin.route("/flot_chart/")
# def flot_chart():
#     return render_template("admin/flot_chart.html")


# 登录
@admin.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！", "err")
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        session["admin_id"] = admin.id
        adminloginlog = AdminLoginLog(
            admin_id=admin.id,
            ip=request.remote_addr,
        )
        db.session.add(adminloginlog)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


# 退出登录
@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("admin.login"))


@admin.route("/index/")
@admin_login_req
@admin_auth
def index():
    """首页"""
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="查看主页")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/index.html")


"""生丝水分控制"""


# 影响因素
@admin.route("/influence/")
@admin_login_req
@admin_auth
def influence():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="查看影响因素")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/influence.html")


def ensure_not_none(value, default=""):
    if value is not None:
        return value
    return default


# 报警控制
@admin.route("/police/")
@admin_login_req
@admin_auth
def police():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="进行报警控制")
    db.session.add(oplog)
    db.session.commit()
    bj_control: BjControl = BjControl.get_last_one()
    data = {}
    if bj_control is not None:
        data["sshc_cksfup"] = ensure_not_none(bj_control.sshc_cksfup)
        data["sshc_cksfdown"] = ensure_not_none(bj_control.sshc_cksfdown)
        data["yjl_rksfup"] = ensure_not_none(bj_control.yjl_rksfup)
        data["yjl_rksfdown"] = ensure_not_none(bj_control.yjl_rksfdown)
        data["yjl_cljzlup"] = ensure_not_none(bj_control.yjl_cljzlup)
        data["yjl_cljzldown"] = ensure_not_none(bj_control.yjl_cljzldown)
        data["yjl_cssllup"] = ensure_not_none(bj_control.yjl_cssllup)
        data["yjl_csslldown"] = ensure_not_none(bj_control.yjl_csslldown)
        data["yjl_lywdup"] = ensure_not_none(bj_control.yjl_lywdup)
        data["yjl_lywddown"] = ensure_not_none(bj_control.yjl_lywddown)
        data["yjl_ljjslup"] = ensure_not_none(bj_control.yjl_ljjslup)
        data["yjl_ljjsldown"] = ensure_not_none(bj_control.yjl_ljjsldown)
        data["yjl_ssjslup"] = ensure_not_none(bj_control.yjl_ssjslup)
        data["yjl_ssjsldown"] = ensure_not_none(bj_control.yjl_ssjsldown)
        data["yjl_wdup"] = ensure_not_none(bj_control.yjl_wdup)
        data["yjl_wddown"] = ensure_not_none(bj_control.yjl_wddown)
        data["yjl_sdup"] = ensure_not_none(bj_control.yjl_sdup)
        data["yjl_sddown"] = ensure_not_none(bj_control.yjl_sddown)
        data["yjl_ckwdup"] = ensure_not_none(bj_control.yjl_ckwdup)
        data["yjl_ckwddown"] = ensure_not_none(bj_control.yjl_ckwddown)
        data["yjl_cksfup"] = ensure_not_none(bj_control.yjl_cksfup)
        data["yjl_cksfdown"] = ensure_not_none(bj_control.yjl_cksfdown)
        data["cy_wdup"] = ensure_not_none(bj_control.cy_wdup)
        data["cy_wddown"] = ensure_not_none(bj_control.cy_wddown)
        data["cy_sdup"] = ensure_not_none(bj_control.cy_sdup)
        data["cy_sddown"] = ensure_not_none(bj_control.cy_sddown)
        data["qs_wdup"] = ensure_not_none(bj_control.qs_wdup)
        data["qs_wddown"] = ensure_not_none(bj_control.qs_wddown)
        data["qs_sdup"] = ensure_not_none(bj_control.qs_sdup)
        data["qs_sddown"] = ensure_not_none(bj_control.qs_sddown)
    return render_template("admin/police.html", data=data)


# 人工干预
@admin.route("/people/")
@admin_login_req
@admin_auth
def people():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="进行人工干预")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/people.html")


"""可视化分析"""


# 温度可视化
@admin.route("/temp_visual/")
@admin_login_req
@admin_auth
def temp_visual():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="温度可视化")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/temp_visual.html")


# 湿度可视化
@admin.route("/humidity_visual/")
@admin_login_req
@admin_auth
def humidity_visual():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="湿度可视化")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/humidity_visual.html")


"""统计查询"""


# 查询
@admin.route("/select/")
@admin_login_req
@admin_auth
def select():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="查询数据情况")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/select.html")


# 统计
@admin.route("/statistics/")
@admin_login_req
@admin_auth
def statistics():
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="查看统计情况")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/statistics.html")


"""用户管理"""


# 添加管理员
@admin.route("/admin/add/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def admin_add():
    form = AdminForm()
    from werkzeug.security import generate_password_hash
    
    if form.validate_on_submit():
        data = form.data
        admin = Admin(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            role_id=data["role_id"],
            is_super=0,
        )
        db.session.add(admin)
        db.session.commit()
        flash("管理员添加成功!", "ok")
        oplog = Oplog(
            admin_id=session["admin_id"],
            ip=request.remote_addr,
            reason="添加管理员{}".format(data["name"]),
        )
        db.session.add(oplog)
        db.session.commit()
        return redirect(url_for("admin.admin_add"))
    return render_template("admin/admin_add.html", form=form)


# 管理员列表
@admin.route("/admin/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def admin_list(page=None):
    if page is None:
        page = 1
    page_data = (
        Admin.query.join(Role)
            .filter(Role.id == Admin.role_id)
            .order_by(Admin.addtime.desc())
            .paginate(page=page, per_page=10)
    )
    oplog = Oplog(
        admin_id=session["admin_id"], ip=request.remote_addr, reason="查看管理员列表"
    )
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/admin_list.html", page_data=page_data)


# 修改密码
@admin.route("/pwd/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=session["admin"]).first()
        from werkzeug.security import generate_password_hash
        
        admin.pwd = generate_password_hash(data["new_pwd"])
        db.session.add(admin)
        db.session.commit()
        flash("密码修改成功,请重新登录!", "ok")
        oplog = Oplog(
            admin_id=session["admin_id"], ip=request.remote_addr,
            reason="进行密码修改"
        )
        db.session.add(oplog)
        db.session.commit()
        return redirect(url_for("admin.logout"))
    return render_template("admin/pwd.html", form=form)


"""权限管理"""


# 添加权限
@admin.route("/auth/add/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def auth_add():
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth_name = Auth.query.filter_by(name=data["name"]).count()
        auth_url = Auth.query.filter_by(url=data["url"]).count()
        if auth_name == 1:
            flash("名称已存在！", "err")
            return redirect(url_for("admin.auth_add"))
        elif auth_url == 1:
            flash("地址已存在！", "err")
            return redirect(url_for("admin.auth_add"))
        else:
            auth = Auth(name=data["name"], url=data["url"])
            db.session.add(auth)
            db.session.commit()
            flash("权限添加成功!", "ok")
            oplog = Oplog(
                admin_id=session["admin_id"],
                ip=request.remote_addr,
                reason="添加权限{}".format(data["name"]),
            )
            db.session.add(oplog)
            db.session.commit()
            return redirect(url_for("admin.auth_add"))
    return render_template("admin/auth_add.html", form=form)


# 权限列表
@admin.route("/auth/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def auth_list(page=None):
    if page is None:
        page = 1
    page_data = Auth.query.order_by(Auth.addtime.desc()).paginate(
        page=page, per_page=10
    )
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="查看权限列表")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/auth_list.html", page_data=page_data)


# 删除权限
@admin.route("/auth/del/<int:id>/", methods=["GET"])
@admin_login_req
@admin_auth
def auth_del(id=None):
    auth = Auth.query.filter_by(id=id).first_or_404()
    db.session.delete(auth)
    db.session.commit()
    flash("删除权限成功!", "ok")
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="删除权限")
    db.session.add(oplog)
    db.session.commit()
    return redirect(url_for("admin.auth_list", page=1))


# 编辑权限
@admin.route("/auth/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def auth_edit(id=None):
    form = AuthForm()
    auth = Auth.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        auth.url = data["url"]
        auth.name = data["name"]
        db.session.add(auth)
        db.session.commit()
        flash("权限修改成功!", "ok")
        redirect(url_for("admin.auth_edit", id=id))
        oplog = Oplog(
            admin_id=session["admin_id"], ip=request.remote_addr, reason="编辑权限"
        )
        db.session.add(oplog)
        db.session.commit()
    return render_template("admin/auth_edit.html", form=form, auth=auth)


"""角色管理"""


# 添加角色
@admin.route("/role/add/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def role_add():
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        role = Role(
            name=data["name"],
            auths=",".join(map(lambda v: str(v), data["auths"]))
        )
        db.session.add(role)
        db.session.commit()
        flash("角色添加成功!", "ok")
        oplog = Oplog(
            admin_id=session["admin_id"],
            ip=request.remote_addr,
            reason="添加角色{}".format(data["name"]),
        )
        db.session.add(oplog)
        db.session.commit()
    return render_template("admin/role_add.html", form=form)


# 角色列表
@admin.route("/role/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def role_list(page=None):
    if page is None:
        page = 1
    page_data = Role.query.order_by(Role.addtime.desc()).paginate(
        page=page, per_page=10
    )
    print("page_data:", page_data)
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="查看角色列表")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/role_list.html", page_data=page_data)


# 删除角色
@admin.route("/role/del/<int:id>/", methods=["GET"])
@admin_login_req
@admin_auth
def role_del(id=None):
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    flash("角色删除成功!", "ok")
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr,
                  reason="删除角色")
    db.session.add(oplog)
    db.session.commit()
    return redirect(url_for("admin.role_list", page=1))


# 编辑角色
@admin.route("/role/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def role_edit(id=None):
    form = RoleForm()
    role = Role.query.get_or_404(id)
    if request.method == "GET":
        auths = role.auths
        form.auths.data = list(map(lambda x: int(x), auths.split(",")))
    if form.validate_on_submit():
        data = form.data
        role.name = data["name"]
        role.auths = ",".join(map(lambda v: str(v), data["auths"]))
        db.session.add(role)
        db.session.commit()
        flash("角色修改成功!", "ok")
        oplog = Oplog(
            admin_id=session["admin_id"], ip=request.remote_addr, reason="编辑角色"
        )
        db.session.add(oplog)
        db.session.commit()
    return render_template("admin/role_edit.html", form=form, role=role)


"""维护管理"""


# 操作日志列表
@admin.route("/oplog/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def oplog_list(page=None):
    if page is None:
        page = 1
    page_data = (
        Oplog.query.join(Admin)
            .filter(
            Admin.id == Oplog.admin_id,
        )
            .order_by(Oplog.addtime.desc())
            .paginate(page=page, per_page=10)
    )
    return render_template("admin/oplog_list.html", page_data=page_data)


# 登录日志列表
@admin.route("/adminloginlog/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def adminloginlog_list(page=None):
    if page is None:
        page = 1
    page_data = (
        AdminLoginLog.query.join(Admin)
            .filter(
            Admin.id == AdminLoginLog.admin_id,
        )
            .order_by(AdminLoginLog.addtime.desc())
            .paginate(page=page, per_page=10)
    )
    return render_template("admin/adminloginlog_list.html", page_data=page_data)
