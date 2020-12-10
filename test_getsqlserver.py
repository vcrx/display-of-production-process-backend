from app.pull.models import Z1Tags, Z2Tags
from app import create_app
from app.models import *
from app.pull import DatabaseManagement

# Z1（松散回潮工段） Sshc
# Z2（润叶加料工段） Yjl
# KLD（烘丝工段）   Hs


app = create_app("db")
app.app_context().push()


dm = DatabaseManagement()

max_time_item = dm.query(Z1Tags).order_by(Z1Tags._TIMESTAMP).first()
print("max_time_item: ", max_time_item)
