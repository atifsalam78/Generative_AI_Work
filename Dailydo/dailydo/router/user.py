from fastapi import APIRouter, Depends, HTTPException
from dailydo.models import Register_User
from typing import Annotated
from dailydo.auth import hash_password, get_user_from_db, oauth_scheme
from dailydo.models import User, Register_User
from sqlmodel import Session
from dailydo.db import get_session

user_router : APIRouter = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description":"Not Found"}}
)

@user_router.get("/")
async def read_user():
    return {"message":"Welcome to daily todo app user page"}

@user_router.post("/register")
async def register_user(new_user : Annotated[Register_User, Depends()],
                        session:Annotated[Session, Depends(get_session)]):
    db_user = get_user_form_db(session, new_user.username, new_user.email)
    if db_user:
        raise HTTPException(status_code=409, details="User already available with these credentials")
    user = User(username = new_user.username,
                email = new_user.email,
                password = hash_password(new_user.password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message":f"User with {user.username} successfully registered"}

# @user_router.get("/me")
# async def user_profile(current_user:Annotated[User, Depends(oauth_scheme)]):
#     return {"hello":"world"}



