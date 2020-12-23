from app.models.control import BjRecords
from datetime import timedelta

import pandas as pd

from sqlalchemy import desc
from flask import current_app

from typing import Union, Type
from .db import DatabaseManagement
from .models import Z1Tags, Z2Tags, KLDTags

from app.constants import plc_uri

N_MINUTES = 1


def judge_alarm(df, MYSQL):
    # MYSQL: Type[Union[Sshc, Yjl, Hs]]
    from app.models import BjControl
    from app.schemas import BjControlSchema

    bj_control = BjControl.get_last_one()
    tablename = MYSQL.__tablename__
    if tablename == "hs":
        prefix = "sssf"
    else:
        prefix = tablename
    if bj_control is None:
        return
    data: dict = BjControlSchema(only=BjControl.get_columns_by_prefix(prefix)).dump(
        bj_control
    )
    result = MYSQL.judge_limit(df, data)
    if result:
        BjRecords.add_one(result)


def migrate_into(MSSQL: Type[Union[Z1Tags, Z2Tags, KLDTags]]):
    from app.models import Hs, Sshc, Yjl, Pch

    """
    MSSQL: Z1Tags, Z2Tags, KLDTags
    MYSQL: Sshc, Yjl, Hs
    """
    log_message = ""
    # 每个数据库的对应关系
    # Z1（松散回潮工段） Sshc
    # Z2（润叶加料工段） Yjl
    # KLD（烘丝工段）   Hs
    if MSSQL == Z1Tags:
        MYSQL = Sshc
    elif MSSQL == Z2Tags:
        MYSQL = Yjl
    elif MSSQL == KLDTags:
        MYSQL = Hs
    else:
        return "无法识别的采集数据库表名"

    s_name = MSSQL.__tablename__
    m_name = MYSQL.__tablename__
    log_message += f" {s_name} -> {m_name} \n"

    dm = DatabaseManagement(plc_uri)

    max_time_item = MYSQL.query.order_by(desc(MYSQL.time)).first()

    query_ = dm.query(MSSQL)

    if max_time_item:
        max_time = max_time_item.time
    else:
        # 说明此时实时数据库中并没有数据
        # 所以直接获取 SQLServer 数据库中的数据
        # 这里是要判断当前数据库中最新的时间
        if current_app.config["SCHEDULER_COLLECTION_FROM_SCRATCH"]:
            # 如果允许了从头取，那就取数据库中最小的时间
            s_item = query_.order_by(MSSQL._TIMESTAMP).first()
        else:
            # 降序取，取数据库中最大的时间
            s_item = query_.order_by(desc(MSSQL._TIMESTAMP)).first()
        if not s_item:
            #  SQLServer 数据库中没数据，直接返回
            log_message += f"{s_name} 表中无数据"
            return log_message
        # 因为后面的时间判断使用 > 号，所以这里要让 max_time 小一点
        max_time = s_item._TIMESTAMP - timedelta(minutes=1)

    # 获取大于已有数据库时间的 N_MINUTES 条数据
    query_ = query_.filter(MSSQL._TIMESTAMP > max_time).filter(
        max_time + timedelta(minutes=N_MINUTES) >= MSSQL._TIMESTAMP
    )
    log_message += f"实时 {m_name} 数据库最新时间: {max_time}\n"
    df = pd.read_sql_query(
        query_.statement,
        dm.session.connection(),
    )
    if df.empty:
        log_message += f"判断无新增数据\n"
        return log_message
    judge_alarm(df, MYSQL)

    grouped_by_time = df.groupby("_TIMESTAMP")
    for time_str in grouped_by_time.groups.keys():
        log_message += f"新增时间 {time_str}\n"

    MYSQL.add_many(df)
    log_message += "Migrate Done."
    return log_message
