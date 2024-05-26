from fastapi import APIRouter, Request, Form
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
async def create_item(title: str = Form(...), desc: str = Form(...)):
    with Session(engine) as session:
        note = Notes(title=title, desc=desc)
        session.add(note)
        session.commit()
    return {"Note" : True}