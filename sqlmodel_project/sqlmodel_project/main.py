from sqlmodel import Field, SQLModel, create_engine, Session, select
from dotenv import load_dotenv
import os

load_dotenv()

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

obj1 : Hero = Hero()
obj1.name = "Muhammad Hashir"
obj1.secret_name = "HAS"
obj1.age = 15

obj2 : Hero = Hero()
obj2.name = "Muhammad Hammdan"
obj2.secret_name = "HAM"
obj2.age = 8

# sqlite_file_name = "database.db" # If we are working with sql lite
# sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(str(os.environ.get("db_key")), echo=False)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
        session.add(obj1)
        session.add(obj2)

        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)

select_heroes()
