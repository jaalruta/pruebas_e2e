import os
from flask import Flask
from flask import abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from modelos import db
from vistas import VistaSignUp, VistaLogIn, VistaInfoUsuario, VistaPing

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
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    abort(401)

@jwt.invalid_token_loader
def invalid_token_callback(error):
    abort(401)

@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    abort(400)



api.add_resource(VistaSignUp, '/users')
api.add_resource(VistaLogIn, '/users/auth')
api.add_resource(VistaInfoUsuario, '/users/me')
api.add_resource(VistaPing, '/users/ping')




