from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mergington High School" in response.text

def test_signup():
    response = client.post("/activities/soccer/signup", params={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully signed up!"}