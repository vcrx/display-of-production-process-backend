from app.models.realtime import Yjl
from app.models.control import BjControl
from app.models.history import YjlInfo
from app import ma


class YjlSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Yjl


class BjControlSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BjControl


class YjlInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = YjlInfo
