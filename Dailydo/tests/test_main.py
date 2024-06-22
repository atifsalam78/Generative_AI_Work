from fastapi.testclient import TestClient
from fastapi import FastAPI
from dailydo import setting
from sqlmodel import SQLModel, create_engine, Session
from dailydo.main import app, get_session


#engine is one for whole application
connection_string : str = str(setting.TEST_DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode" : "require"}, pool_recycle=300, pool_size=10, echo=True)
#by default pool size is 5 by sqlAlchemy, pool_recycle means destroy the connection after 300 seconds if not in use and create new

#Test-1: root test
def test_root():
    client = TestClient(app=app)
    response = client.get("/")
    data = response.json()
    assert response.status_code == 200
    assert data == {"message" : "Welcom to Daily Do App!"}

#Test-2: post test
def test_create_todo():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app=app)
    test_todo = {"content":"create todo test", "is_completed":False}
    response = client.post("/todos/", json=test_todo)
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == test_todo["content"]

#Test-3: get_all test
def test_get_all():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app=app)
    test_todo = {"content":"get all todos test", "is_completed":False}
    response = client.post("/todos/", json=test_todo)
    data = response.json()

    response = client.get("/todos/")
    new_todo = response.json()[-1]
    assert response.status_code == 200
    assert new_todo["content"] == test_todo["content"]

#Test-4: Single tood test
def test_get_single_todo():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app=app)

    test_todo = {"content":"get single todo test", "is_completed":False}
    response = client.post("/todos/", json=test_todo)
    todo_id = response.json()["id"]

    response = client.get(f"/todos/{todo_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == test_todo["content"]

#Test-5: edit todo test
def test_edit_todo():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app=app)

    test_todo = {"content":"edit single todo test", "is_completed":False}
    response = client.post("/todos/", json=test_todo)
    todo_id = response.json()["id"]

    edited_todo = test_todo = {"content":"we have edited this", "is_completed":False}
    response = client.put(f"/todos/{todo_id}", json=edited_todo)
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == edited_todo["content"]

#Test-6: delete todo test
def test_delete_todo():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app=app)

    test_todo = {"content":"delete todo test", "is_completed":False}
    response = client.post("/todos/", json=test_todo)
    todo_id = response.json()["id"]

    response = client.delete(f"/todos/{todo_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "Task has been successfully deleted"









