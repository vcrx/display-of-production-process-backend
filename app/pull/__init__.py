from app.models.realtime import Pch
from datetime import timedelta

import arrow
import pandas as pd
from app.models import Hs, Sshc, Yjl
from app.pull.db import DatabaseManagement
from app.pull.models import Z1Tags, Z2Tags
from sqlalchemy import desc

# Z1（松散回潮工段） Sshc
# Z2（润叶加料工段） Yjl
# KLD（烘丝工段）   Hs

N_MINITES = 1


def migrate_into(SqlserverDatabaseModel, MysqlDatabaseModel):
    """
    SqlserverDatabaseModel: Z1Tags, Z2Tags
    MysqlDatabaseModel: Sshc, Yjl, Hs
    """
    assert SqlserverDatabaseModel in (Z1Tags, Z2Tags)
    assert MysqlDatabaseModel in (Sshc, Yjl, Hs)
    s_name = SqlserverDatabaseModel.__tablename__
    m_name = MysqlDatabaseModel.__tablename__
    print(f" {s_name} -> {m_name} ")

    dm = DatabaseManagement()

    max_time_item = MysqlDatabaseModel.query.order_by(
        desc(MysqlDatabaseModel.time)
    ).first()

    query_ = dm.query(SqlserverDatabaseModel)

    # 获取大于已有数据库时间的 N_MINITES 条数据
    if max_time_item:
        max_time = max_time_item.time
    else:
        # 说明此时实时数据库中并没有数据
        # 所以直接获取 SQLServer 数据库中的几分钟的数据
        # s_item = query_.order_by(desc(SqlserverDatabaseModel._TIMESTAMP)).first()
        s_item = query_.order_by((SqlserverDatabaseModel._TIMESTAMP)).first()
        if not s_item:
            #  SQLServer 数据库中没数据，直接返回
            return
        # 因为后面的时间判断使用 > 号，所以这里要让 max_time 小一点
        max_time = s_item._TIMESTAMP - timedelta(minutes=1)

    query_ = query_.filter(SqlserverDatabaseModel._TIMESTAMP > max_time).filter(
        max_time + timedelta(minutes=N_MINITES) >= SqlserverDatabaseModel._TIMESTAMP
    )
    print(f"实时 {m_name} 数据库最新时间: ", max_time)
    df = pd.read_sql_query(
        query_.statement,
        con=dm.session.connection(),
    )
    if df.empty:
        print("无新增数据")
        return 0
    pch = Pch.get(m_name)
    qualified = (df["_QUALITY"] == 192).all()
    print("采集数据是否合格: ", qualified)
    print("pch: ", pch)
    # 合格数据将放到上一批，否则批次号将+1
    if not qualified:
        Pch.set(m_name, pch + 1)
        pch = pch + 1
        print("批次号+1", pch)
    grouped_by_time = df.groupby("_TIMESTAMP")
    result = {}
    """
    result 的结构大概如下：
    {
        '2020/10/12 13:06': {
            'DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_03.OutPhyPV': {
                '_NUMERICID': 0.0,
                '_VALUE': 18.793315889,
                '_QUALITY': 192.0
            },
            ...
        },
    }
    """
    for time_str in grouped_by_time.groups.keys():
        print("新增时间:", time_str)
        data = (
            grouped_by_time.get_group(time_str)
            .groupby("_BATCHID")
            .mean()
            .drop("id", axis=1)
            .T.to_dict()
        )
        time_arrow = arrow.get(time_str).datetime
        result[time_arrow] = data
    MysqlDatabaseModel.add_many(result)
