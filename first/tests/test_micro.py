from fastapi.testclient import TestClient
from first.micro_app import app

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello" : "World"}

def test_todo():
    client = TestClient(app=app)
    response = client.get("/todo/")
    assert response.status_code == 200
    assert response.json() == {"App" : "ToDo"}

def test_todo_second():
    client = TestClient(app=app)
    response = client.get("/todo/")
    assert response.status_code == 200
    assert response.json() == {"App" : "ABC"}



