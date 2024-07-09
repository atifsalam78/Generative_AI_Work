from fastapi import FastAPI

app : FastAPI = FastAPI(
    title = "Hello World",
    version = "0.0.1",
     servers=[
        {
            "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/todo/")
def todo():
    return {"App" : "ToDo"}