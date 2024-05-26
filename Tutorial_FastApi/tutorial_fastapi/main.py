from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Field, SQLModel, create_engine, Session, select
from dotenv import load_dotenv
import os

load_dotenv()

class Notes(SQLModel, table=True):
    note_id : int = Field(default=None, primary_key=True)
    title : str
    desc : str

# obj1 : Notes = Notes()
# obj1.title = "My Third Note Title"
# obj1.desc = "This is my third note"

# obj2 : Notes = Notes()
# obj2.title = "My Fourth Note Title"
# obj2.desc = "This is my fourth note"



engine = create_engine(str(os.environ.get("db_key")), echo = False)
SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(obj1)
#     session.add(obj2)

#     session.commit()

newNote : list = []

def select_notes():
    with Session(engine) as session:
        statement = select(Notes)
        results = session.exec(statement)
        for note in results:
            if note not in newNote:
                newNote.append({
                "title" : note.title
                })




app : FastAPI = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request:     Request):
    select_notes()
    return templates.TemplateResponse(name="index.html", context={"request": request, "newNote" : newNote})


# @app.get("/items/{item_id}")
# async def read_item(item_id : int, q : str | None = None):
#     q = "My Personal Id"
#     return {"item_id" : item_id, "q" : q}