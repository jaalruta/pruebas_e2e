import os
from flask import Flask
from flask import abort
from flask_cors import CORS
from flask_restful import Api

from modelos import db
from vistas import VistaRoutes, VistaPing , VistaRoute

USER = "docker" if os.getenv('USER_DB_P') is None else os.getenv('USER_DB_P')
PASSWORD = "docker" if os.getenv('PASSWORD_DB_P') is None else os.getenv('PASSWORD_DB_P')
HOST = "localhost" if os.getenv('HOST_DB_P') is None else os.getenv('HOST_DB_P')
DB = "microservicio" if os.getenv('DB_P') is None else os.getenv('DB_P')
PORT = "9002" if os.getenv('DB_P_PORT') is None else os.getenv('DB_P_PORT')

DB_HOST = HOST+":"+PORT
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+USER+':'+PASSWORD+'@'+DB_HOST+'/'+DB
app.config['PROPAGATE_EXCEPTIONS'] = True
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
cors = CORS(app)
api = Api(app)

api.add_resource(VistaRoutes, '/routes/')
api.add_resource(VistaRoute, '/routes/<id>')
api.add_resource(VistaPing, '/routes/ping')
