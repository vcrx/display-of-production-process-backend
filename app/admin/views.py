import datetime
from functools import wraps

from flask import render_template, redirect, url_for, flash, session, abort, request

from app import db
from app.admin.forms import LoginForm, PwdForm, AuthForm, RoleForm, AdminForm, AlarmForm
from app.models import Admin, Auth, Role, AdminLoginLog, Oplog, RgControl, Yjl, Sshc, Hs
from app.models import BjControl
from app.schemas import BjControlSchema
from app.utils import safe_float
from . import admin
from ..utils.time import extract_search_from_args


# 上下文应用处理器
@admin.context_processor
def tpl_extra():
    data = dict(online_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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
            .filter(Role.id == Admin.role_id, Admin.id == session["admin_id"])
            .first()
        )
        auths = admin.role.auths
        auths = list(map(lambda x: int(x), auths.split(",")))
        auth_list = Auth.query.all()
        # 当前用户可访问的 url
        urls = [v.url for v in auth_list for val in auths if val == v.id]
        rule = request.url_rule
        block_flag = True
        for url in urls:
            # 只要求前缀存在就行。
            # 比如 /hello/<name> 和 /hello 两个规则只需要设置 /hello 就行
            # if str(rule) == url:
            if str(rule).startswith(url):
                block_flag = False
                break
        if block_flag:
            print(str(rule) + " is blocked because auth fail")
            abort(401)
        return func(*args, **kwargs)

    return decorated_function


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
    oplog = Oplog(admin_id=session["admin_id"], ip=request.remote_addr, reason="查看主页")
    db.session.add(oplog)
    db.session.commit()
    return render_template("admin/index.html")


# 报警控制
@admin.route("/alarm/", methods=("GET", "POST"))
@admin_login_req
@admin_auth
def alarm():
    form = AlarmForm()
    bj_control: BjControl = BjControl.get_last_one()

    if request.method == "GET":
        Oplog.add_one("查看报警控制")
    else:
        Oplog.add_one("修改报警控制")
        if form.validate_on_submit():
            form_data = {}
            for key, value in request.form.items():
                if key != "csrf_token":
                    form_data[key] = safe_float(form.data.get(key))
            obj = bj_control or BjControl()
            obj.update(**form_data)
            db.session.add(obj)
            db.session.commit()
            flash("修改成功", "alarm-success")
        else:
            flash("修改失败", "alarm-error")
        return redirect(url_for("admin.alarm"))
    data = {}
    if bj_control is not None:
        data: dict = BjControlSchema().dump(bj_control)
        # 让前端展示 None 为 空字符串
        for k, v in data.items():
            if v is None:
                data[k] = ""
    return render_template("admin/alarm.html", data=data, form=form)


# 人工干预
@admin.route("/manual/list/<int:page>/")
@admin_login_req
@admin_auth
def manual(page=None):
    Oplog.add_one("人工干预")
    if page is None:
        page = 1

    rg_query = RgControl.query
    search, dt = extract_search_from_args()
    if dt.get("from"):
        rg_query = rg_query.filter(RgControl.create_at >= dt.get("from"))
    if dt.get("to"):
        rg_query = rg_query.filter(RgControl.create_at <= dt.get("to"))

    page_data = rg_query.order_by(RgControl.create_at.desc()).paginate(
        page=page, per_page=10
    )
    return render_template("admin/manual.html", page_data=page_data, search=search)


# 温度可视化
@admin.route("/temp_visual/")
@admin_login_req
@admin_auth
def temp_visual():
    Oplog.add_one("温度可视化")
    return render_template("admin/temp_visual.html")


# 湿度可视化
@admin.route("/humidity_visual/")
@admin_login_req
@admin_auth
def humidity_visual():
    Oplog.add_one("湿度可视化")
    return render_template("admin/humidity_visual.html")


# 查询
@admin.route("/query/list/<int:page>/")
@admin.route("/query/list/<int:page>/<factor>/")
@admin_login_req
@admin_auth
def query(page=None, factor=None):
    if page is None:
        page = 1
    if factor is None:
        factor = "sshc"
    if factor not in ["sshc", "ryjl", "hs"]:
        print(factor)
        abort(404)

    Oplog.add_one("查询数据情况")

    search, dt = extract_search_from_args()

    def query_wrapper(model):
        tmp_query = model.query
        if dt.get("from"):
            tmp_query = tmp_query.filter(model.time >= dt.get("from"))
        if dt.get("to"):
            tmp_query = tmp_query.filter(model.time <= dt.get("to"))
        tmp_data = tmp_query.order_by(model.id.desc()).paginate(page=page, per_page=10)
        return tmp_data

    yjl_data = None
    if factor == "ryjl":
        yjl_data = query_wrapper(Yjl)
    sshc_data = None
    if factor == "sshc":
        sshc_data = query_wrapper(Sshc)
    hs_data = None
    if factor == "hs":
        hs_data = query_wrapper(Hs)

    return render_template(
        "admin/query.html",
        hash=factor,
        yjl_data=yjl_data,
        sshc_data=sshc_data,
        hs_data=hs_data,
        search=search,
    )


# 统计
@admin.route("/statistics/")
@admin_login_req
@admin_auth
def statistics():
    Oplog.add_one("查看统计情况")
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
        Oplog.add_one("添加管理员{}".format(data["name"]))
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
        .order_by(Admin.create_at.desc())
        .paginate(page=page, per_page=10)
    )
    Oplog.add_one("查看管理员列表")
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
        Oplog.add_one("进行密码修改")
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
            Oplog.add_one("添加权限{}".format(data["name"]))
            return redirect(url_for("admin.auth_add"))
    return render_template("admin/auth_add.html", form=form)


# 权限列表
@admin.route("/auth/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def auth_list(page=None):
    if page is None:
        page = 1
    page_data = Auth.query.order_by(Auth.create_at.desc()).paginate(
        page=page, per_page=10
    )
    Oplog.add_one("查看权限列表")
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
    Oplog.add_one("删除权限" + str(id))
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
        Oplog.add_one("编辑权限" + str(data))
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
            name=data["name"], auths=",".join(map(lambda v: str(v), data["auths"]))
        )
        db.session.add(role)
        db.session.commit()
        flash("角色添加成功!", "ok")
        Oplog.add_one("添加角色{}".format(data["name"]))
    return render_template("admin/role_add.html", form=form)


# 角色列表
@admin.route("/role/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def role_list(page=None):
    if page is None:
        page = 1
    page_data = Role.query.order_by(Role.create_at.desc()).paginate(
        page=page, per_page=10
    )
    Oplog.add_one("查看角色列表" + str(page))
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
    Oplog.add_one("删除角色" + str(id))
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
        Oplog.add_one("编辑角色" + str(id))
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
        .order_by(Oplog.create_at.desc())
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
        .filter(Admin.id == AdminLoginLog.admin_id)
        .order_by(AdminLoginLog.create_at.desc())
        .paginate(page=page, per_page=10)
    )
    return render_template("admin/adminloginlog_list.html", page_data=page_data)
