"""
文档：
https://docs.sqlalchemy.org/en/14/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc

使用 Hostname-based connections
"""
from urllib.parse import quote_plus
from sqlalchemy.engine.url import URL
from copy import copy

# 使用 hostname 连接时，要指定使用的 Driver 名字
sqlserver_driver = "SQL Server Native Client 10.0"

db_uri = URL(
    "mssql+pyodbc",
    username="sa",
    password="My.Password",
    host="127.0.0.1",
    port=1433,
    query={"charset": "utf8", "driver": sqlserver_driver},
)


def database(name):
    _db_uri = copy(db_uri)
    _db_uri.database = name
    return _db_uri


# 程序需要使用的数据库
yancao_db_uri = database("yancao")

# 原有的采集数据的数据库
origin_db_uri = database("test")
