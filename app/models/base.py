from app import db
from datetime import datetime


class Base(db.Model):
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now,
                          onupdate=datetime.now)
