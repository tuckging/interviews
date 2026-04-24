import json
    
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_item():
    response = client.post("/items/1", params={"item": json.dumps({"type": "item", "name": "Test Item"})})
    assert response.status_code == 200

def test_create_item_uuid():
    response = client.post("/items/123e4567-e89b-12d3-a456-426614174000", params={"item": json.dumps({"type": "item", "name": "Test Item"})})
    assert response.status_code == 200
