import os
from flask import Flask
from flask import abort
from flask_cors import CORS
from flask_restful import Api

from modelos import db
from vistas import VistaRoutes, VistaPing , VistaRoute

USER = os.getenv('USER_DB_P')
PASSWORD = os.environ.get('PASSWORD_DB_P')
HOST = os.environ.get('HOST_DB_P')
DB = os.environ.get('DB_P')
PORT = os.environ.get('DB_P_PORT')

if not USER:
    USER = 'user'

if not PASSWORD:
    PASSWORD = 'pass1234'

if not HOST:
    HOST = 'localhost'

if not DB:
    DB = 'microservicio'
if not PORT:
    PORT = '5432'

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
