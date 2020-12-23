import pandas as pd
from app.pull.models import History
from app.models import *
from app.pull import DatabaseManagement, qs_mapping


from app.constants import mes_uri
import arrow


mes_dm = DatabaseManagement(mes_uri)

start = arrow.get("2020-12-16 10:56:23").datetime
end = arrow.get("2020-12-16 14:56:23").datetime
q = History.query(mes_dm, start, end, qs_mapping.values()).all()
df = pd.read_sql_query(
    q.statement,
    mes_dm.session.connection(),
)
print("df: ", df)

result = mes_dm.execute_sql(
    """select *
from openquery(InSQL, 'select datetime, [DLNY_ArchestrA_KT_K1.AIValue.23], [DLNY_ArchestrA_KT_K1.AIValue.24]
from widehistory
where DateTime>=''2020-12-16 10:56:23.133''
  and DateTime<=''2020-12-16 14:56:23.133''
  and wwRetrievalMode=''cyclic''
  and wwResolution=30000')"""
)
names = [row[0] for row in result]
print("names: ", names)

for r in result:
    print(r[0])
    r_dict = dict(r.items())  # convert to dict keyed by column names

result = mes_dm.execute_sql(
    """select *
from dbo.History
where TagName='DLNY_ArchestrA_KT_K1.AIValue.23'
  and wwRetrievalMode = 'Cyclic'
  and wwResolution = 30000
  and datetime between '2020-12-16 10:56:23.133' and '2020-12-16 14:56:23.133'"""
)
names = [row[0] for row in result]
print("names: ", names)

for r in result:
    print(r[0])
    r_dict = dict(r.items())  # convert to dict keyed by column names



"""
-- 1
select *
from openquery(InSQL, 'select datetime, [DLNY_ArchestrA_KT_K1.AIValue.23], [DLNY_ArchestrA_KT_K1.AIValue.24]
from widehistory
where DateTime>=''2020-12-16 10:56:23.133''
  and DateTime<=''2020-12-16 14:56:23.133''
  and wwRetrievalMode=''cyclic''
  and wwResolution=30000')


-- 2
select *
from dbo.History
where TagName='DLNY_ArchestrA_KT_K1.AIValue.23'
  and wwRetrievalMode = 'Cyclic'
  and wwResolution = 30000
  and datetime between '2020-12-16 10:56:23.133' and '2020-12-16 14:56:23.133'

"""
