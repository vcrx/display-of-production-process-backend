import pandas as pd

front_display_mapping = {
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_PV_Massflow": "松散回潮物料实际流量",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_SP_Massflow": "松散回潮物料设定流量",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_Total_Massflow": "松散回潮物料累计重量",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.TB101_PV_Temperature": "松散回潮回风温度",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Moisture": "松散回潮出口水分",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Temp": "松散回潮出口温度",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_PV_Massflow": "润叶加料物料实际流量",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_SP_Massflow": "润叶加料物料设定流量",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_Total_Massflow": "润叶加料物料累计重量",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ST201_Total_Waterflow": "润叶加料实时累计加水量",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF201_PV_Moisture": "润叶加料入口水分",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_03.OutPhyPV": "润叶加料瞬时加水量",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_04.OutPhyPV": "润叶加料瞬时加料量",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.KA104_PV_ST201_Temperature": "润叶加料料液温度",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Temp": "润叶加料出口温度",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Moisture": "润叶加料出口水分",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.SP_SteamMaFl": "烘丝蒸汽流量设定流量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_SP": "烘丝物料设定流量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.MOIST_PV": "生丝水分",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamMaFl": "烘丝蒸汽流量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamPressAft": "烘丝阀后蒸汽压力",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamPressBef": "烘丝阀前蒸汽压力",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamVolFl": "烘丝蒸汽体积",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_ValPos_Y32": "烘丝Y32阀门值",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_PV": "烘丝物料实际流量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_TOT": "烘丝物料累计重量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.CV_SteamMaFl": "烘丝蒸汽流量阀门开度",
}

# 烘丝工段
kld_mapping = {
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamMaFl": "SX增温增湿机 蒸汽流量 实际值",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamVolFl": "SX增温增湿机 蒸汽体积",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamPressBef": "SX增温增湿机 阀前 蒸汽压力",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_SteamPressAft": "SX增温增湿机 阀后 蒸汽压力",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.PV_ValPos_Y32": "SX增温增湿机 Y32阀门 实际值",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.SX1_HMI.Misc.Value.SP_SteamMaFl": "SX增温增湿机 蒸汽流量 设定值",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_PV": "SX增温增湿机 皮带秤 实际流量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_SP": "SX增温增湿机 皮带秤 设定流量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.FLOW_TOT": "SX增温增湿机 皮带秤 累计量",
    "DietDAServer.Tags.KLD.PLC.ProgramBlock.HMI.Component.Upstream_HMI.Misc.Value.MOIST_PV": "SX增温增湿机 入口水分 实际值",
}
# 松散回潮工段
z1_mapping = {
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_SP_Massflow": "松散回潮 皮带秤 设定值",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_PV_Massflow": "松散回潮 皮带秤 实际值",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.TB101_PV_Temperature": "松散回潮 回风温度 实际值",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Moisture": "松散回潮 水分仪 ZF102 出口水分 实际值",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_Temp": "松散回潮 水分仪 ZF102 出口温度 实际值",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.ZF102_PV_B1_Trim": "松散回潮 水分仪 ZF102 出口水分 调零值",
    "DietDAServer.Tags.Z1.PLC.Global.HMI_Wr_ShowValue.RB101_Total_Massflow": "松散回潮 皮带秤 总量",
}
# 润叶加料工段
z2_mapping = {
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_03.OutPhyPV": "润叶加料 加水流量 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_04.OutPhyPV": "润叶加料 加料流量 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_PIDState_x.HMI_Wr_PIDState_05.OutPhyPV": "备用",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_PV_Massflow": "润叶加料 皮带秤 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_SP_Massflow": "润叶加料 皮带秤 设定值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.DB201_Total_Massflow": "润叶加料 皮带秤 累计值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.KA103_PV_ST201_Temperature": "KA103 料液温度 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.KA104_PV_ST201_Temperature": "KA104 料液温度 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.KA105_PV_ST201_Temperature": "KA105 料液温度 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ST201_PV_TemP": "ST201 料液温度 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ST201_Total_Waterflow": "润叶加料 加水总量 累计值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF201_PV_Moisture": "润叶加料 入口水分 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Moisture": "润叶加料 出口水分 实际值",
    "DietDAServer.Tags.Z2.PLC.Global.HMI_Wr_ShowValue.ZF202_PV_Temp": "润叶加料 出口温度 实际值",
}
