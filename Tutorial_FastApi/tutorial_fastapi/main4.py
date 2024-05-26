from fastapi import FastAPI, Header
from typing import Annotated


app : FastAPI = FastAPI()

# @app.get("/hi")
# def greet(who:str = Header()):
#     return f"Hello, {who}"

# @app.get("/agent")
# # def get_agent(user_agent:str = Header()): # Old Version
# def get_agent(user_agent : Annotated[str | None, Header()] = None): # New upgraded version
#     return user_agent

# @app.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header()] = None):
#     return {"User-Agent": user_agent}

# Duplicate Headers

@app.get("/items/")
async def read_items(x_token:Annotated[list[str] | None, Header()]= None):
    return {"x_token": x_token}