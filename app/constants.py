"""
sqlserver 数据库文档：
https://docs.sqlalchemy.org/en/14/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc
"""
from sqlalchemy.engine.url import URL
from copy import copy


# sqlserver 数据库的地址
base_sqlserver_uri = URL(
    "mssql+pyodbc",
    username="sa",
    password="My.Password",
    host="127.0.0.1",
    port=1433,
    query={
        "charset": "utf8",
        # 使用 hostname 连接时，要指定使用的 Driver 名字
        "driver": "SQL Server Native Client 10.0",
    },
)
# mysql 数据库的地址
base_mysql_server = URL(
    "mysql+pymysql",
    username="root",
    password="root",
    host="127.0.0.1",
    port=3306,
)


def database(db_uri, name):
    _db_uri = copy(db_uri)
    _db_uri.database = name
    return _db_uri


# 原有的采集数据的数据库
sqlserver_uri = database(base_sqlserver_uri, "test")

# 程序需要使用的数据库
mysql_uri = database(base_mysql_server, "yancao")
