from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql import func

db = SQLAlchemy()

class Trayecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sourceAirportCode = db.Column(db.String(200))
    sourceCountry  = db.Column(db.String(1000))
    destinyAirportCode  = db.Column(db.String(1000))
    destinyCountry  = db.Column(db.String(1000))
    bagCost  = db.Column(db.Integer)
    expireAt  = db.Column(db.DateTime)
    createdAt  = db.Column(db.DateTime,server_default=func.now())


class TrayectoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Trayecto
        include_relationships = True
        load_instance = True
