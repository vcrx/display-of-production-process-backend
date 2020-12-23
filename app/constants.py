"""
mssql 数据库文档：
https://docs.sqlalchemy.org/en/14/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc
"""
from os import getenv as _

from sqlalchemy.engine.url import URL

# 原有的采集数据的数据库
plc_uri = URL(
    "mssql+pyodbc",
    username="sa",
    password=_("PLC_PASSWORD"),
    host="127.0.0.1",
    port=1433,
    database="MYAlarmTagSystem",
    query={
        "charset": "utf8",
        # 使用 hostname 连接时，要指定使用的 Driver 名字
        "driver": "SQL Server Native Client 10.0",
    },
)

# 温湿度数据库
mes_uri = URL(
    "mssql+pyodbc",
    username="sa",
    password=_("MES_PASSWORD"),
    host="127.0.0.1",
    port=1433,
    database="Runtime",
    query={
        "charset": "utf8",
        # 使用 hostname 连接时，要指定使用的 Driver 名字
        "driver": "SQL Server Native Client 10.0",
    },
)

# mysql 数据库的地址
mysql_uri = URL(
    "mysql+pymysql",
    username="root",
    password=_("MYSQL_PASSWORD"),
    host="127.0.0.1",
    port=3306,
    database="yancao",
)
