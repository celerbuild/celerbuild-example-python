from fastapi.testclient import TestClient
from app.main import app

# Create test client
client = TestClient(app)

def test_read_root():
    # Test root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from CelerBuild!"}

def test_read_version():
    # Test version endpoint
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}