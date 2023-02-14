import pytest
import responses
from app import app as flask_app

@pytest.fixture(scope='session')
def app():
    yield flask_app
    
@pytest.fixture(scope='session')
def client(app):
    responses.start()
    responses.add(responses.GET,
        'http://localhost:5005/users/me',
        status=200
    )
    app.config['TESTING'] = True
    client = app.test_client() 
    yield client
    responses.stop()

