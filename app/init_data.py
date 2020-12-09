import sys
from pathlib import Path

import arrow
import pandas as pd

from app import create_app
from app.models import *

app = create_app("db")
app.app_context().push()

data_dir = Path(__file__).parent.parent / "data"
print("data_dir:", data_dir)


def get_data(csv_name):
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

    grouped_by_time = df.groupby("_TIMESTAMP")
    result = {}
    for time_str in grouped_by_time.groups.keys():
        data = (
            grouped_by_time.get_group(time_str)
            .groupby("_BATCHID")
            .mean()
            .drop("id", axis=1)
            .T.to_dict()
        )
        time_arrow = arrow.get(time_str).datetime
        result[time_arrow] = data
    return result


z1 = get_data(data_dir / "Z1（松散回潮工段）.csv")
z2 = get_data(data_dir / "Z2（润叶加料工段）.csv")
kld = get_data(data_dir / "KLD（烘丝工段）.csv")

print("正在添加：Z1（松散回潮工段）.csv")
Sshc.add_many(z1)
print("正在添加：Z2（润叶加料工段）.csv")
Yjl.add_many(z2)
print("正在添加：KLD（烘丝工段）.csv")
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
    "松散回潮出口水分均值": "cksf",
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
    "润叶加料料液温度均值": "ly_wd",
}
cy_columns = {
    "日期": "rq",
    "品牌号": "pph",
    "批次号": "pch",
    "润叶加料贮叶时间": "cysc",
    "sirox增温增湿sirox入口水分均值": "sssf",
    "储叶房温度": "wd",
    "储叶房湿度": "sd",
}
qs_columns = {"日期": "rq", "品牌号": "pph", "批次号": "pch", "储丝房温度": "wd", "储丝房湿度": "sd"}


def gen_data_list(type_dict, whole_df: pd.DataFrame) -> list:
    result = []
    # 确保 type_dict.keys() 的值都在 df 里面，手动过滤一遍
    available_keys = list(filter(lambda x: x in whole_df.columns, type_dict.keys()))
    for idx, data in whole_df[available_keys].iterrows():
        data_dict = data.to_dict()
        tmp = {}
        # data_dict 拿到的是 dataframe 转出来的 dict, 字典键还是中文的
        # 转成英文键方便后续使用
        for cn_name, en_name in type_dict.items():
            # 把日期转为 arrow 格式，方便之后使用
            if en_name == "rq":
                v = data_dict.get(cn_name)
                if v is not None:
                    tmp[en_name] = arrow.get(v).datetime
                else:
                    tmp[en_name] = None
            else:
                tmp[en_name] = data_dict.get(cn_name)
        result.append(tmp)
    return result


root = data_dir / "生丝水分数据csv/"
for file in root.iterdir():
    if file.suffix == ".csv":
        print("正在处理： " + str(file))
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

sys.exit(0)
