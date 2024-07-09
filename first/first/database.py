from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://Invoice_owner:LK0N1TJdtVGU@ep-small-firefly-a1opfutt.ap-southeast-1.aws.neon.tech/userlogin?sslmode=require"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

