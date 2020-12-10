from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class Base(object):
    def __repr__(self) -> str:
        return "<{} id={} batchid={} timestamp={}>".format(
            self.__tablename__, self.id, self._BATCHID, self._TIMESTAMP
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base = declarative_base(cls=Base)


class Z1Tags(Base):
    __tablename__ = "Z1Tags"
    id = Column(Integer(), primary_key=True, nullable=False)
    _BATCHID = Column(String(200))
    _NUMERICID = Column(Integer())
    _VALUE = Column(Float())
    _TIMESTAMP = Column(DateTime())
    _QUALITY = Column(Integer())


class Z2Tags(Base):
    __tablename__ = "Z2Tags"
    id = Column(Integer(), primary_key=True, nullable=False)
    _BATCHID = Column(String(200))
    _NUMERICID = Column(Integer())
    _VALUE = Column(Float())
    _TIMESTAMP = Column(DateTime())
    _QUALITY = Column(Integer())


if __name__ == "__main__":
    from .db import DatabaseManagement

    dm = DatabaseManagement()
    dm.create_database(Base.metadata)