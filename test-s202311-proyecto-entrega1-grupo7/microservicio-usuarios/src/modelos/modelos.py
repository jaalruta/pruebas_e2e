from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql import func

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    email  = db.Column(db.String(1000))
    password  = db.Column(db.String(1000))
    salt  = db.Column(db.String(1000))
    token  = db.Column(db.String(1000))
    expireAt  = db.Column(db.DateTime)
    createdAt  = db.Column(db.DateTime,server_default=func.now())


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True
