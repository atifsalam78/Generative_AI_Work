from fastapi import FastAPI
from enum import Enum

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# print(Color.RED)
# print(Color(1))
# print(Color.RED.value)


app : FastAPI = FastAPI() # Instance of class FastAPI


# @app.get("/items/{item_id}") # Path operation decorator, is also called endpoint or route
# async def read_item(item_id: int):# Path operation function
#     return {"item_id": item_id}

# Path Parameters


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id" : "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id : str):
#     return {"user_id" : user_id}


# @app.get("/users")
# async def read_user():
#     return ["Rick", "Morty"]

# @app.get("/users")
# async def read_user2():
#     return ["Bean", "Alpha"]



# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"



# @app.get("/models/{model_name}")
# async def get_model(model_name : ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model": model_name, "message": "Deep Learning FTW!"}
    
#     if model_name.value == "lenet":
#         return {"model": model_name, "message": "LeCNN all the images"}
    
#     return {"model": model_name, "message": "Have some residuals"}


# Query Parameters

# @app.get("/file/{file_path:path}")
# async def read_file(file_path : str):
#     return {"file_path" : file_path}


# fake_list_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : " Baz"}]

# @app.get("/items/")
# async def read_item(skip : int = 0, limit : int = 10):
#     return fake_list_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id : str, q: str | None = None):
#     if q:
#         return {"item_id" : item_id, "q" : q}
#     return {"item_id" : item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id : str, q : str | None = None, short : bool = False):
#     item = {"item_id" : item_id}
#     if q:
#         item.update({"q" : q})
#     if not short:
#         item.update({"description" : "This is an amazing item has long description"})

#     return item


@app.get("/items/{item_id}")
async def read_user_item(item_id : str, need : str):
    item = {"item_id" : item_id, "needy" : need}
    return item