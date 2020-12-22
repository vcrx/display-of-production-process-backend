from app.models.realtime import Yjl, Hs, Sshc
from app.models.control import BjControl, BjRecords, RgControl
from app.models.history import YjlInfo
from app import ma


class YjlSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Yjl


class HsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hs


class SshcSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sshc


class BjControlSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BjControl


class BjRecordsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BjRecords


class YjlInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = YjlInfo


class RgControlSchema(ma.SQLAlchemySchema):
    class Meta:
        model = RgControl

    ljjsl = ma.auto_field()
    sssf = ma.auto_field()
    cysc = ma.auto_field()
