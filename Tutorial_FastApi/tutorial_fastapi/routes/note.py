from fastapi import APIRouter, Request
from models.note import Note
from fastapi.responses import HTMLResponse
from sqlmodel import Field, SQLModel, create_engine, Session, select
from fastapi.templating import Jinja2Templates
from config.db import engine
from schemas.note import noteEntity, notesEntity
from typing import Any

note : APIRouter = APIRouter()

templates = Jinja2Templates(directory="templates")

class Notes(SQLModel, table=True):
    note_id : int = Field(default=None, primary_key=True)
    title : str | None = None
    desc : str | None = None


newNote : list = []

def select_notes():
    with Session(engine) as session:
        statement = select(Notes)
        results = session.exec(statement)
        
        for note in results:
            if {"title" : note.title} not in newNote:
                newNote.append({"title" : note.title})               



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    select_notes()
    return templates.TemplateResponse(name="index.html", context={"request": request, "newNote" : newNote})


@note.post("/")
async def create_item(request : Request) -> Any:
    return {"Note" : True}

# @note.post("/", response_class=HTMLResponse)
# async def creat_item(request : Request):
#     form = await request.form()
#     with Session(engine) as session:
#         session.add(dict[form])
#         session.commit()
#         return {"Sucess" : True}
    



# @note.post("/heroes/", response_model=HTMLResponse)
# async def create_hero(request: Request):
#     form = await request.form()
#     with Session(engine) as session:
#         db_note = Note.model_validate(request)
#         session.add(db_note)
#         session.commit()
#         session.refresh(db_note)
#         return db_note


# obj1 : Notes = Notes()
# obj1.title = "My Third Note Title"
# obj1.desc = "This is my third note"

# with Session(engine) as session:
#     session.add(obj1)
#     session.add(obj2)

#     session.commit()


# @note.post("/")
# async def add_note(note: Note):
#     with Session(engine) as session:
#         inserted_note = session.add(dict(note))
#         session.commit()
#         return noteEntity(inserted_note)