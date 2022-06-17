"""
Module with database structure definition
"""
from config import db, ma
import re
from sqlalchemy.dialects.sqlite import DATETIME

# Datetime format used in the metrobuses data source at:
# https://datos.cdmx.gob.mx/datastore/dump/ad360a0e-b42f-482c-af12-1fd72140032e?bom=True
dt = DATETIME(
    storage_format = "%(year)04d-%(month)02d-%(day)02d"
                    "T%(hour)02d:%(minute)02d:%(second)02d",
    regexp = r"(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+)"
)


class Metrobus(db.Model):
    __tablename__ = "metrobuses"
    _id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    date_updated = db.Column(dt, nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)
    vehicle_label = db.Column(db.Integer, nullable=False)
    vehicle_current_status = db.Column(db.Integer, nullable=False)
    position_latitude = db.Column(db.Float, nullable=False)
    position_longitude = db.Column(db.Float, nullable=False)
    geographic_point = db.Column(db.String, nullable=False)
    position_speed = db.Column(db.Integer, nullable=False)
    position_odometer = db.Column(db.Integer, nullable=False)
    trip_schedule_relationship = db.Column(db.Integer, nullable=False)
    trip_id = db.Column(db.Integer, nullable=True)
    trip_start_date = db.Column(db.Integer, nullable=True)
    trip_route_id = db.Column(db.Integer, nullable=True)

class MetrobusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Metrobus
        load_instance = True

class Alcaldia(db.Model):
    __tablename__ = "alcaldias"
    _id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    nomgeo = db.Column(db.String, nullable=False)
    cve_mun = db.Column(db.Integer, nullable=False)
    cve_ent = db.Column(db.Integer, nullable=False)
    cvegeo = db.Column(db.Integer, nullable=False)
    geo_point_2d = db.Column(db.String, nullable=False)
    geo_shape = db.Column(db.String, nullable=False)
    municipio = db.Column(db.Integer, nullable=False)

class AlcaldiaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Alcaldia
        load_instance = True
