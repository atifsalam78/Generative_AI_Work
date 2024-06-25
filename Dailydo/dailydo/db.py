from sqlmodel import SQLModel, Field, create_engine, Session
from dailydo import setting

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

