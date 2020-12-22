from app.pull.models import Z1Tags, Z2Tags
from app import create_app
from app.models import *
from app.pull import migrate_into

# Z1（松散回潮工段） Sshc
# Z2（润叶加料工段） Yjl
# KLD（烘丝工段）   Hs


app = create_app("db")
app.app_context().push()

migrate_into(Z1Tags)
migrate_into(Z2Tags)
