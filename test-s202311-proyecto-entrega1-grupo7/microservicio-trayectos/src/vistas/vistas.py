from operator import eq
from flask import request,abort,make_response
from flask_restful import Resource
from sqlalchemy import desc,asc,func
from datetime import datetime ,timedelta
from modelos import db,Trayecto, TrayectoSchema
import json
import os
import requests
import sys
tayecto_schema = TrayectoSchema()

class VistaRoutes(Resource):


    def post(self):

        if request.headers.get('Authorization') == None or not validaUsuario(request.headers.get('Authorization')):
            abort(401)

        if request.json == None or not "sourceAirportCode" in request.json or not "sourceCountry" in request.json or not "destinyAirportCode" in request.json or not "destinyCountry" in request.json or not "bagCost" in request.json:
            abort(400)
        else:

            token = request.headers.get('Authorization')
            sourceAirportCode = request.json["sourceAirportCode"]
            sourceCountry = request.json["sourceCountry"]
            destinyAirportCode = request.json["destinyAirportCode"]
            destinyCountry = request.json["destinyCountry"]
            bagCost = request.json["bagCost"]

            basedir = os.path.abspath(os.path.dirname(__file__))
            data_file = os.path.join(basedir, 'IATA.json')

            file = open(data_file)
            IATA = json.load(file)
            file.close()


            if sourceAirportCode not in IATA or destinyAirportCode not in IATA:
                abort(400)
            trayecto = Trayecto.query.filter(Trayecto.sourceAirportCode == sourceAirportCode , Trayecto.destinyAirportCode == destinyAirportCode , Trayecto.expireAt >= datetime.now().date()).first()
            if trayecto is not None:
                if trayecto.expireAt.date() > datetime.now().date():
                    abort(412)

            expira = datetime.now() + timedelta(days=30)
            nuevo_trayecto = Trayecto(sourceAirportCode=sourceAirportCode, sourceCountry=sourceCountry,  destinyAirportCode=destinyAirportCode, destinyCountry=destinyCountry,bagCost=bagCost , expireAt = expira)
            db.session.add(nuevo_trayecto)
            db.session.commit()
            return {"id": nuevo_trayecto.id,"createdAt": nuevo_trayecto.createdAt.strftime("%d/%m/%Y") , "expireAt": nuevo_trayecto.expireAt.strftime("%d/%m/%Y")} , 201
        
    def get(self):

        if request.headers.get('Authorization') == None or not validaUsuario(request.headers.get('Authorization')):
            abort(401)
        
        sourceAirportCode = request.args.get('from')
        destinyAirportCode = request.args.get('to')
        fecha = request.args.get('when')

        trayectos = Trayecto.query

        if sourceAirportCode is not None:
            trayectos = trayectos.filter(Trayecto.sourceAirportCode == sourceAirportCode)
        if destinyAirportCode is not None:
            trayectos = trayectos.filter(Trayecto.destinyAirportCode == destinyAirportCode)
        if fecha is not None:
            try:
                fecha_busqueda = datetime.strptime(fecha, '%d/%m/%Y')
            except:
                abort(400)
            trayectos = trayectos.filter(fecha_busqueda.date() >=  func.date(Trayecto.createdAt)  ,  fecha_busqueda.date() <= func.date(Trayecto.expireAt) )
        trayectos = trayectos.all()

        respuesta = []

        for trayecto in trayectos:
            respuesta.append(
                {
                    "id": trayecto.id,
                    "sourceAirportCode":trayecto.sourceAirportCode,
                    "sourceCountry":trayecto.sourceCountry,
                    "destinyAirportCode":trayecto.destinyAirportCode,
                    "destinyCountry":trayecto.destinyCountry,
                    "bagCost":trayecto.bagCost
                })
        
        return respuesta , 200



class VistaRoute(Resource):
    
    def get(self,id):
        if request.headers.get('Authorization') == None or not validaUsuario(request.headers.get('Authorization')):
            abort(401)
        
        try:
            filtro = int(id)        
        except:
            abort(400)
        
        trayecto = Trayecto.query.filter(Trayecto.id == filtro).first()
        if trayecto is None:
            abort(404)
        

        return  {"id": trayecto.id,"sourceAirportCode":trayecto.sourceAirportCode,"sourceCountry":trayecto.sourceCountry,"destinyAirportCode":trayecto.destinyAirportCode,"destinyCountry":trayecto.destinyCountry,"bagCost":trayecto.bagCost}, 200

class VistaPing(Resource):

    def get(self):
        response = make_response("pong", 200)
        response.mimetype = "text/plain"
        return response


def validaUsuario(token):

    token = token.split()[1]
    USER_SERVICE_PROTOCOL = os.environ.get('USER_SERVICE_PROTOCOL')
    USER_SERVICE_NAME = os.environ.get('USER_SERVICE_NAME')
    USER_SERVICE_PORT = os.environ.get('USER_SERVICE_PORT')

    res = requests.get(USER_SERVICE_PROTOCOL+"://"+USER_SERVICE_NAME+":"+USER_SERVICE_PORT+'/users/me', headers={"Authorization": "Bearer {}".format(token)})
    if res.status_code == 200:
        return True
    else:
        return False
        


        
        

