from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from .base import Base as _Base


class Base(_Base):
    def __repr__(self) -> str:
        return "<{} id={} batchid={} timestamp={}>".format(
            self.__tablename__, self.id, self._BATCHID, self._TIMESTAMP
        )


Base = declarative_base(cls=Base)


class Z1Tags(Base):
    """Z1（松散回潮工段） Sshc"""

    __tablename__ = "Z1Tags"
    id = Column(Integer(), primary_key=True, nullable=False)
    _BATCHID = Column(String(200))
    _NUMERICID = Column(Integer())
    _VALUE = Column(Float())
    _TIMESTAMP = Column(DateTime())
    _QUALITY = Column(Integer())


class Z2Tags(Base):
    """Z2（润叶加料工段） Yjl"""

    __tablename__ = "Z2Tags"
    id = Column(Integer(), primary_key=True, nullable=False)
    _BATCHID = Column(String(200))
    _NUMERICID = Column(Integer())
    _VALUE = Column(Float())
    _TIMESTAMP = Column(DateTime())
    _QUALITY = Column(Integer())


class KLDTags(Base):
    """KLD（烘丝工段）   Hs"""

    __tablename__ = "KLDTags"
    id = Column(Integer(), primary_key=True, nullable=False)
    _BATCHID = Column(String(200))
    _NUMERICID = Column(Integer())
    _VALUE = Column(Float())
    _TIMESTAMP = Column(DateTime())
    _QUALITY = Column(Integer())


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
