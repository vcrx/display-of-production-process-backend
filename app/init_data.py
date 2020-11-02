import pandas as pd
from app.utils.convert import getData
from app import db
from app.models import *

z1 = getData("../data/Z1（松散回潮工段）.csv")
z2 = getData("../data/Z2（润叶加料工段）.csv")
kld = getData("../data/KLD（烘丝工段）.csv")

Sshc.add_many(z1)
Yjl.add_many(z2)
Hs.add_many(kld)
