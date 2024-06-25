from passlib.context import CryptContext
from sqlmodel import Session, select
from typing import Annotated
from dailydo.db import get_session
from fastapi import Depends
from dailydo.models import User, Todo
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta 


SECRET_KEY = "ed607gasgdsagdasdgj343gretutgjc45i57y5c745yi457y4"
ALGORITHYM = "HS256"
EXPIRY_TIME = 30

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")
pwd_context = CryptContext(schemes="bcrypt")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)

def get_user_from_db (session:Annotated[Session, Depends(get_session)],
                      username: str):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()

    if not user:
        statement = select(User).where(User.username == username)
        session.exec(statement).first()
        if user:
            return user

    return user

def authenticate_user(username,
                      password,                      
                      session:Annotated[Session, Depends(get_session)]):
    db_user = get_user_from_db(session=session, username=username)
    print(f"""authenticate {db_user}""")
    if not db_user:
        return False
    if not verify_password(password, db_user.password):
        return False
    return db_user

def create_access_token(data:dict, expiry_time:timedelta|None):
    data_to_encode = data.copy()
    if expiry_time:
        expire = datetime.now(timezone.utc) + expiry_time
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    data_to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHYM)
    return encoded_jwt
    
