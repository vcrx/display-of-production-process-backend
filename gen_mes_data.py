import itertools
from app.pull.models import History
from app import create_app
from app.models import *
from app.pull import migrate_into, DatabaseManagement
from random import random

# Z1（松散回潮工段） Sshc
# Z2（润叶加料工段） Yjl
# KLD（烘丝工段）   Hs

from app.constants import plc_uri, mes_uri

# app = create_app("db")
# app.app_context().push()

mes_dm = DatabaseManagement(mes_uri)
from datetime import datetime, timedelta

now = datetime.now()

li = [
    "DLNY_ArchestrA_KT_K2.AIValue.36",
    "DLNY_ArchestrA_KT_K2.AIValue.37",
    "DLNY_ArchestrA_KT_K2.AIValue.32",
    "DLNY_ArchestrA_KT_K2.AIValue.33",
    "DLNY_ArchestrA_KT_K3.AIValue.0",
    "DLNY_ArchestrA_KT_K3.AIValue.1",
    "DLNY_ArchestrA_KT_K2.AIValue.0",
    "DLNY_ArchestrA_KT_K2.AIValue.1",
]

l = len(li)
_i = 0
sequence = (x // 2 + 1 for x in itertools.count())

for _ in range(100):
    i = next(sequence)
    n_time = now + timedelta(minutes=i)
    h = History(DateTime=n_time, wwResolution=30000, wwRetrievalMode="Cyclic")
    h.TagName = li[_i % l]
    h.Value = random()
    _i = _i + 1
    mes_dm.session.add(h)

mes_dm.session.commit()
