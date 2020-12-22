from os import getenv

from app.constants import plc_uri, mysql_uri
from sqlalchemy.exc import InterfaceError
from sqlalchemy_utils import database_exists, create_database


def database_exists_(url):
    try:
        return database_exists(url)
    except InterfaceError:
        return False


def init_database(db_uri):
    if not database_exists_(db_uri):
        print(f"create {db_uri}")
        create_database(db_uri)
    print(f"{db_uri} exists:", database_exists_(db_uri))


init_database(mysql_uri)


from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import *

from app.pull import DatabaseManagement
from app.pull.models import Base

if getenv("NEED_INIT_MSSQL"):
    init_database(plc_uri)
    dm = DatabaseManagement(plc_uri)
    dm.create_database(Base.metadata)

app = create_app("db")
context = app.app_context()
context.push()

db.create_all()
db.session.add(Auth(id="1", name="主路由", url="/"))
db.session.add(Auth(id="2", name="首页", url="/index/"))
db.session.add(Auth(id="3", name="生丝水分控制-报警控制", url="/alarm/"))
db.session.add(Auth(id="4", name="生丝水分控制-人工干预", url="/manual/list/<int:page>/"))
db.session.add(Auth(id="5", name="可视化分析-温度可视化", url="/temp_visual/"))
db.session.add(Auth(id="6", name="可视化分析-湿度可视化", url="/humidity_visual/"))
db.session.add(Auth(id="7", name="统计查询-查询", url="/query/list/<int:page>/"))
db.session.add(Auth(id="8", name="统计查询-统计", url="/statistics/"))
db.session.add(Auth(id="9", name="用户管理-添加管理员", url="/admin/add/"))
db.session.add(Auth(id="10", name="用户管理-管理员列表", url="/admin/list/<int:page>/"))
db.session.add(Auth(id="11", name="修改密码", url="/pwd/"))
db.session.add(Auth(id="12", name="权限管理-添加权限", url="/auth/add/"))
db.session.add(Auth(id="13", name="权限管理-权限列表", url="/auth/list/<int:page>/"))
db.session.add(Auth(id="14", name="权限管理-删除权限", url="/auth/del/<int:id>/"))
db.session.add(Auth(id="15", name="权限管理-编辑权限", url="/auth/edit/<int:id>/"))
db.session.add(Auth(id="16", name="角色管理-添加角色", url="/role/add/"))
db.session.add(Auth(id="17", name="角色管理-角色列表", url="/role/list/<int:page>/"))
db.session.add(Auth(id="18", name="角色管理-删除角色", url="/role/del/<int:id>/"))
db.session.add(Auth(id="19", name="角色管理-编辑角色", url="/role/edit/<int:id>/"))
db.session.add(Auth(id="20", name="维护管理-操作日志列表", url="/oplog/list/<int:page>/"))
db.session.add(Auth(id="21", name="维护管理-登录日志列表", url="/adminloginlog/list/<int:page>/"))
db.session.commit()

role = Role(
    id=1, name="超级管理员", auths="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21"
)
admin = Admin(
    name="admin",
    pwd=generate_password_hash("admin"),
    email="admin@example.com",
    phone=1111,
    role_id=role.id,
    is_super=0,
)
db.session.add(role)
db.session.add(admin)
db.session.commit()

print("`init_db` Done.")

context.pop()
