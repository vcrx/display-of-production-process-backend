import pandas as pd
from app import db
from app.models import *
from pathlib import Path


def getData(csv_name):
    """
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
    df = pd.read_csv(csv_name, encoding="gbk")
    df.drop(df.columns[-1], axis=1, inplace=True)
    
    grouped = df.groupby("_TIMESTAMP")
    result = {}
    for key in grouped.groups.keys():
        data = (
            grouped.get_group(key)
                .groupby("_BATCHID")
                .mean()
                .drop("id", axis=1)
                .T.to_dict()
        )
        result[key] = data
    return result


z1 = getData("../data/Z1（松散回潮工段）.csv")
z2 = getData("../data/Z2（润叶加料工段）.csv")
kld = getData("../data/KLD（烘丝工段）.csv")

Sshc.add_many(z1)
Yjl.add_many(z2)
Hs.add_many(kld)

sshc_columns = {
    "日期": "rq",
    "品牌号": "pph",
    "批次号": "pch",
    "松散回潮皮带秤实时流量均值": "wlssll",
    "松散回潮皮带秤累计值": "wlljzl",
    "松散回潮累计加水量": "ljjsl",
    "松散回潮回风温度均值": "hfwd",
    "松散回潮出口温度均值": "ckwd",
    "松散回潮出口水分均值": "cksf"
}
yjl_columns = {
    "日期": "rq",
    "品牌号": "pph",
    "批次号": "pch",
    "润叶加料入口水分均值": "rksf",
    "润叶加料皮带秤实时流量均值": "wlssll",
    "润叶加料皮带秤累计值": "wlljzl",
    "润叶加料出口水分均值": "cksf",
    "润叶加料出口温度均值": "ckwd",
    "润叶加料累计加水量": "ljjsl",
    "润叶加料料液流量实时流量均值": "ly_ssll",
    "润叶加料料液流量累计加料量": "ly_ljjl",
    "润叶加料料液温度均值": "ly_wd"
}
cy_columns = {
    "日期": "rq",
    "品牌号": "pph",
    "批次号": "pch",
    "润叶加料贮叶时间": "cysc",
    "sirox增温增湿sirox入口水分均值": "sssf",
    "储叶房温度": "wd",
    "储叶房湿度": "sd"
}
qs_columns = {
    "日期": "rq",
    "品牌号": "pph",
    "批次号": "pch",
    "储丝房温度": "wd",
    "储丝房湿度": "sd"
}


def gen_data_list(type_dict, whole_df: pd.DataFrame) -> list:
    result = []
    # 确保 type_dict.keys() 的值都在 df 里面，手动过滤一遍
    available_keys = list(
        filter(lambda x: x in whole_df.columns, type_dict.keys()))
    for idx, data in whole_df[available_keys].iterrows():
        data_dict = data.to_dict()
        tmp = {}
        # data_dict 拿到的是 dataframe 转出来的 dict, 字典键还是中文的
        # 转成英文键方便后续使用
        for key, value in type_dict.items():
            tmp[value] = data_dict.get(key)
        result.append(tmp)
    return result


root = Path("../data/生丝水分数据csv/")
for file in root.iterdir():
    if file.suffix == ".csv":
        df = pd.read_csv(file, encoding="gbk")
        # 过滤 nan
        df = df.where(pd.notnull(df), None)
        yjl_result = gen_data_list(yjl_columns, df)
        sshc_result = gen_data_list(sshc_columns, df)
        cy_result = gen_data_list(cy_columns, df)
        qs_result = gen_data_list(qs_columns, df)
        SshcInfo.add_many(sshc_result)
        YjlInfo.add_many(yjl_result)
        CyInfo.add_many(cy_result)
        QsInfo.add_many(qs_result)
