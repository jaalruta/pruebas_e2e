import json
from urllib.parse import urljoin
from faker import Faker
import time
import responses

fake = Faker()

def test_crea_ruta_sin_token(app,client):
    res = client.post('/routes/')
    assert res.status_code == 401


def test_crea_ruta_cont_token_sin_parametros(app,client):
    res = client.post('/routes/',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 400

def test_crea_ruta_cont_token_sin_algun_parametro(app,client):
    res = client.post('/routes/',json={'sourceCountry': 'COL','destinyAirportCode':"ASU","destinyCountry":"ASU","bagCost":2},headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 400


def test_crear_ruta_iata_invalido(app, client):
    res = client.post('/routes/', json={'sourceAirportCode': "ZZZ", 'sourceCountry': 'COL','destinyAirportCode':"ASU","destinyCountry":"ASU","bagCost":2},headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 400

def test_crear_ruta_repetida(app,client):
    client.post('/routes/', json={'sourceAirportCode': "ARI", 'sourceCountry': 'COL','destinyAirportCode':"ASU","destinyCountry":"ASU","bagCost":2},headers={"Authorization": "Bearer {}".format("12132123132")})
    res = client.post('/routes/', json={'sourceAirportCode': "ARI", 'sourceCountry': 'COL','destinyAirportCode':"ASU","destinyCountry":"ASU","bagCost":2},headers={"Authorization": "Bearer {}".format("12132123132")})
    
    assert res.status_code == 412

def test_crear_ruta_correcta(app,client):
    res = client.post('/routes/', json={'sourceAirportCode': "BBA", 'sourceCountry': 'COL','destinyAirportCode':"ASU","destinyCountry":"ASU","bagCost":2},headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 201

def test_obtiene_rutas_sin_token(app,client):
    res = client.get('/routes/')
    assert res.status_code == 401

def test_obtiene_rutas_sin_parametros(app,client):
    res = client.get('/routes/',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 200

def test_obtiene_rutas_com_parametro_from(app,client):
    res = client.get('/routes/?from=BBA',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 200

def test_obtiene_rutas_com_parametro_to(app,client):
    res = client.get('/routes/?to=COL',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 200

def test_obtiene_rutas_com_parametro_when(app,client):
    res = client.get('/routes/?when=13/02/2023',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 200

def test_obtiene_rutas_com_parametro_when_incorrecto(app,client):
    res = client.get('/routes/?when=DD/MM/YYYY',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 400

def test_obtiene_una_ruta_sin_token(app,client):
    res = client.get('/routes/12')
    assert res.status_code == 401

def test_obtiene_una_ruta_id_no_numero(app,client):
    res = client.get('/routes/dsada',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 400

def test_obtiene_una_ruta_id_no_existente(app,client):
    res = client.get('/routes/-9999',headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 404

def test_obtiene_una_ruta_existente(app,client):

    rutas = client.get('/routes/',headers={"Authorization": "Bearer {}".format("12132123132")}).get_json()
    id = rutas[0]["id"]

    res = client.get('/routes/'+str(id),headers={"Authorization": "Bearer {}".format("12132123132")})
    assert res.status_code == 200

def test_ping(app,client):
    res = client.get('/routes/ping')
    assert res.status_code == 200
    expected = "pong"
    response =  expected in res.get_data(as_text=True)
    assert  response == True