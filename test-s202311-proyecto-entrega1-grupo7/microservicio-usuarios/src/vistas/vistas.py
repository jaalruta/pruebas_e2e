import random
import hashlib
from operator import eq
from flask import request,abort,make_response
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity,get_jwt
from flask_restful import Resource
from sqlalchemy import desc,asc
from datetime import timedelta , datetime
from modelos import db,Usuario, UsuarioSchema

usuario_schema = UsuarioSchema()

class VistaSignUp(Resource):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def post(self):

        if request.json == None or not "username" in request.json or not "password" in request.json or not "email" in request.json:
            abort(400)
        else:
            username = request.json["username"]
            password = request.json["password"]
            email = request.json["email"]

            if (not username or username.isspace()) or (not password or password.isspace()) or (not email or email.isspace())  :
                abort(400)
            if Usuario.query.filter(Usuario.username == request.json["username"]).first() is not None:
                abort(412)
            elif Usuario.query.filter(Usuario.email == request.json["email"]).first() is not None:
                abort(412)
            else:
                salt = ''.join(random.choice(self.ALPHABET) for i in range(16))   
                salt_password = password+salt
                hashed = hashlib.sha256(salt_password.encode('utf-8')).hexdigest()

                nuevo_usuario = Usuario(username=username, password=hashed,  email=email, salt=salt)
                db.session.add(nuevo_usuario)
                db.session.commit()
                return {"id": nuevo_usuario.id,"createdAt": nuevo_usuario.createdAt.strftime("%d/%m/%Y")} , 201

class VistaLogIn(Resource):

    def post(self):
        if request.json == None or not "username" in request.json or not "password" in request.json:
           abort(400)
        username = request.json["username"]
        password = request.json["password"]
        if (not username or username.isspace()) or (not password or password.isspace())  :
            abort(400)
        ##valida si el usuario existe
        usuario = Usuario.query.filter(Usuario.username == username).first()

        
        if usuario is None:
            abort(404)
        else:
            #valida la contraseña
            salt_password = password+usuario.salt
            hashed = hashlib.sha256(salt_password.encode('utf-8')).hexdigest()
            if usuario.password != hashed:
                abort(404)
            else:
                token_de_acceso = create_access_token(identity=usuario.id,expires_delta= timedelta(hours=1))
                expires = datetime.now() + timedelta(hours=1)
                usuario.token = token_de_acceso
                usuario.expireAt = expires
                db.session.commit()
                return {"id": usuario.id, "token": token_de_acceso, "expireAt": expires.strftime("%d/%m/%Y %H:%M:%S")} , 200


class VistaInfoUsuario(Resource):

    @jwt_required()
    def get(self):
        uid = get_jwt_identity()
        usuario = Usuario.query.filter(Usuario.id == uid).first()
        return {"id": usuario.id, "username": usuario.username, "email": usuario.email} , 200

class VistaPing(Resource):

    def get(self):
        response = make_response("pong", 200)
        response.mimetype = "text/plain"
        return response

        


        
        

