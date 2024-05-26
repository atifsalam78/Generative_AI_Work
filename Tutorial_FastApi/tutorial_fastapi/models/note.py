from pydantic import BaseModel

class Note(BaseModel):
    title : str | None = None
    desc : str | None = None
    # important : bool

    