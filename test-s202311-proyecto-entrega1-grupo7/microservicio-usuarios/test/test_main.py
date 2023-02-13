import json
from faker import Faker
fake = Faker()

def test_creacion_usuario_sin_un_parametro(app, client):
    res = client.post('/users', json={'password': fake.password(),'email':fake.email()})
    assert res.status_code == 400

def test_creacion_usuario_nombre_vacio(app, client):
    res = client.post('/users', json={'username': '', 'password': fake.password(),'email':fake.email()})
    assert res.status_code == 400

def test_creacion_usuario_email_vacio(app, client):
    res = client.post('/users', json={'username': fake.user_name(), 'password': fake.password(),'email':''})
    assert res.status_code == 400

def test_creacion_usuario_password_vacio(app, client):
    res = client.post('/users', json={'username': fake.user_name(), 'password': '','email':fake.email()})
    assert res.status_code == 400

def test_creacion_usuario_sin_data(app, client):
    res = client.post('/users')
    assert res.status_code == 400

def test_creacion_usuario_usuario_existente(app, client):
    usuario = fake.user_name()
    #crea el primer usuario
    client.post('/users', json={'username': usuario, 'password': fake.password(),'email':fake.email()})
    #crea el segundo usuario con el mimso username
    res = client.post('/users', json={'username': usuario, 'password': fake.password(),'email':fake.email()})
    assert res.status_code == 412

def test_creacion_usuario_correo_existente(app, client):
    email = fake.email()
    #crea el primer usuario
    client.post('/users', json={'username': fake.user_name(), 'password': fake.password(),'email':email})
    #crea el segundo usuario con el mimso email
    res = client.post('/users', json={'username': fake.user_name(), 'password': fake.password(),'email':email})
    assert res.status_code == 412

def test_creacion_usuario_correcta(app, client):
    res = client.post('/users', json={'username': fake.user_name(), 'password': fake.password(),'email':fake.email()})
    assert res.status_code == 201

def test_login_usuario_sin_un_parametro(app, client):
    res = client.post('/users/auth', json={'password': fake.password()})
    assert res.status_code == 400

def test_login_usuario_usuario_vacio(app, client):
    res = client.post('/users/auth', json={'username': '', 'password': fake.password()})
    assert res.status_code == 400

def test_login_usuario_password_vacio(app, client):
    res = client.post('/users/auth', json={'username': fake.user_name(), 'password': ''})
    assert res.status_code == 400

def test_login_usuario_sin_data(app, client):
    res = client.post('/users/auth')
    assert res.status_code == 400

def test_login_usuario_no_existente(app, client):
    res = client.post('/users/auth', json={'username': fake.user_name(), 'password': fake.password()})
    assert res.status_code == 404

def test_login_usuario_existente_password_invalido(app, client):
    username = fake.user_name()
    #crea el usuario
    client.post('/users', json={'username': username , 'password': fake.password(),'email':fake.email()})
    #intenta login con mismo usuario pero otra clave
    res = client.post('/users/auth', json={'username': username, 'password': fake.password()})
    assert res.status_code == 404

def test_login_usuario_valido(app, client):
    username = fake.user_name()
    password = fake.password()
    #crea el usuario
    client.post('/users', json={'username': username , 'password':password,'email':fake.email()})
    #intenta login con mismo usuario y la misma clave
    res = client.post('/users/auth', json={'username': username, 'password': password})
    assert res.status_code == 200

def test_informacion_usuario_sin_token(app, client):
    res = client.get('/users/me')
    assert res.status_code == 400

def test_informacion_usuario_con_token_invalido(app, client):
    res = client.get('/users/me', headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 401

def test_informacion_usuario_con_token_valido(app, client):
    username = fake.user_name()
    password = fake.password()
    #crea el usuario
    client.post('/users', json={'username': username , 'password':password,'email':fake.email()})
    #intenta login con mismo usuario y la misma clave
    res = client.post('/users/auth', json={'username': username, 'password': password})
    #obtiene el token generado
    token = res.json["token"]
    #realiza la peticion de informacion
    res = client.get('/users/me', headers={"Authorization": "Bearer {}".format(token)})
    assert res.status_code == 200

def test_operacion_ping(app, client):
    res = client.get('/users/ping')
    assert res.status_code == 200
    expected = "pong"
    response =  expected in res.get_data(as_text=True)
    assert  response == True