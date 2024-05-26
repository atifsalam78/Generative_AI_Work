from fastapi import FastAPI


app : FastAPI = FastAPI()

@app.get("/hi/{who}") # Path decorator, It tells FastAPI, request from the url sould be directed to the following function
def greet(who): # endpoint: This is the main point of contact with http request and response
    return f"Hello? {who}"

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", reload=True)