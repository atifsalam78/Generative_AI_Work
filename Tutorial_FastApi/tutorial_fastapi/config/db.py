from sqlmodel import Field, SQLModel, create_engine, Session, select
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(str(os.environ.get("db_key")), echo = False)
SQLModel.metadata.create_all(engine)