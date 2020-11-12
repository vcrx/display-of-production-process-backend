from datetime import datetime
from . import safe_float


# 从毫秒的时间戳转为分钟的 datetime
def from_mills_timestamp_to_min(mills):
    timestamp = int(safe_float(mills) / 1000)
    dt = datetime.fromtimestamp(timestamp)
    dt = dt.replace(second=0, microsecond=0)
    return dt
