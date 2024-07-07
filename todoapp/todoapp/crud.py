from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .datab import get_session
from .models import ToDo, ToDoCreate, ToDoRead, ToDoUpdate

todo_router = APIRouter()

@todo_router.post("/todos/", response_model=ToDoRead)
def create_todo(*, session: Session = Depends(get_session), todo: ToDoCreate):
    db_todo = ToDo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@todo_router.get("/todos/{todo_id}", response_model=ToDoRead)
def read_todo(*, session: Session = Depends(get_session), todo_id: int):
    todo = session.get(ToDo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

# remove list
@todo_router.get("/todos/", response_model=list[ToDoRead])
def read_todos(*, session: Session = Depends(get_session)):
    todos = session.exec(select(ToDo)).all()
    return todos

@todo_router.put("/todos/{todo_id}", response_model=ToDoRead)
def update_todo(*, session: Session = Depends(get_session), todo_id: int, todo: ToDoUpdate):
    db_todo = session.get(ToDo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@todo_router.delete("/todos/{todo_id}", response_model=ToDoRead)
def delete_todo(*, session: Session = Depends(get_session), todo_id: int):
    db_todo = session.get(ToDo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    session.delete(db_todo)
    session.commit()
    return db_todo
