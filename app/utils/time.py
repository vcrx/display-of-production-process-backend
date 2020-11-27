from datetime import datetime
from . import safe_float
from flask import request


# 从毫秒的时间戳转为分钟的 datetime
def from_mills_timestamp_to_min(mills):
    timestamp = int(safe_float(mills) / 1000)
    dt = datetime.fromtimestamp(timestamp)
    dt = dt.replace(second=0, microsecond=0)
    return dt


def extract_search_from_args():
    params = request.args
    
    search = {}
    dt = {}
    time_from = params.get("from")
    time_to = params.get("to")
    
    if time_from is not None and time_to is not None:
        search["from"] = time_from
        search["to"] = time_to
        
        from_ = from_mills_timestamp_to_min(time_from)
        to = from_mills_timestamp_to_min(time_to)
        # 查后一分钟之前的，所以要加一
        to = to.replace(minute=to.minute + 1)
        dt["from"] = from_
        dt["to"] = to
    return search, dt
