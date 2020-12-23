from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .base import Base as _Base

Base = declarative_base(cls=_Base)


class History(Base):
    __tablename__ = "History"
    id = Column(Integer(), primary_key=True, nullable=False)
    DateTime = Column(DateTime())
    TagName = Column(String(256))
    Value = Column(Float())
    wwRetrievalMode = Column(String(16))
    wwResolution = Column(Integer())

    @staticmethod
    def query(dm, start, end, tag_names):
        if type(tag_names) != list:
            tag_names = [tag_names]
        return (
            dm.query(History)
            .filter(History.DateTime.between(start, end))
            .filter_by(wwResolution=30000, wwRetrievalMode="Cyclic")
            .filter(History.TagName.in_(tag_names))
        )
