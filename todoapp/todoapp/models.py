from sqlmodel import SQLModel, Field
from typing import Optional

class ToDoBase(SQLModel):
    title: str
    description: Optional[str] = None

class ToDoCreate(ToDoBase):
    pass

class ToDoRead(ToDoBase):
    id: int

class ToDoUpdate(ToDoBase):
    pass

class ToDo(ToDoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
