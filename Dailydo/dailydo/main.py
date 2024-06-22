#poetry env info --path
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from dailydo import setting
from typing import Annotated
from contextlib import asynccontextmanager

""""
Step-1: Create database on Noen
Step-2: Create .evn file for environment variables
Step-3: Create setting.py file for encrypting Database Url
Step-4: Creat a Model
Step-5: Creat Engine
Step-6: Create Function for table creation
Step-7: Create function for session management
Step-8: Create context manager for app lifespan
Step-9: Create all endpoints for todo app

"""
# Create Model
    # data model
    # table model
# Todo is a child class and will extend it's parent class SQLModel
# This model will use for both data validation and table creation(data model & table model)
class Todo(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    content : str = Field(index=True, min_length=3, max_length=54)
    is_completed : bool = Field(default=False)

#engine is one for whole application
connection_string : str = str(setting.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode" : "require"}, pool_recycle=300, pool_size=10, echo=True)
#by default pool size is 5 by sqlAlchemy, pool_recycle means destroy the connection after 300 seconds if not in use and create new

def create_tables():
    """To create tables in database"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Session management for dpendency injection"""
    with Session(engine) as session:
        yield session

@asynccontextmanager # by using this it's means when our app run this will execute first before any thing
async def lifespan(app:FastAPI):
    """When our app run this will execute first"""
    print("Creating Tables")
    create_tables()
    print("Tables Created")
    yield

app : FastAPI = FastAPI(lifespan=lifespan, title="Daily ToDo App", version="1.0.0")

# End Points for Todo App
@app.get("/")
async def root():
    return {"message" : "Welcom to Daily Do App!"}


@app.post("/todos/", response_model=Todo) # response_model is to use this as data model
async def create_todo(todo:Todo, session:Annotated[Session, Depends(get_session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo 

@app.get("/todos/", response_model= list[Todo])
async def get_all(session:Annotated[Session, Depends(get_session)]):
    # statement = select(Todo)
    todos = session.exec(select(Todo)).all()
    if todos:
        return todos
    else:
        raise HTTPException (status_code=404, detail="No task found")

@app.get("/todos/{id}", response_model=Todo)
async def get_single_todo(id:int, session:Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id==id)).first()
    if todo:
        return todo
    else:
        raise HTTPException (status_code=404, detail="No task found")


@app.put("/todos/{id}")
async def edit_todo(id:int, todo:Todo, session:Annotated[Session, Depends(get_session)]):
    existing_todo = session.exec(select(Todo).where(Todo.id==id)).first()
    if existing_todo:
        existing_todo.content = todo.content
        existing_todo.is_completed = todo.is_completed
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    else:
        raise HTTPException(status_code=404, detail="No task found")

@app.delete("/todos/{id}")
async def delete_todo(id:int, session:Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id==id)).first()
    if todo:
        session.delete(todo)
        session.commit()
        # session.refresh()
        return {"message":"Task has been successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="No task found")