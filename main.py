import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello, World"}

if __name__ == '__main__':
    uvicorn.run("main:app", port=1111, host='127.0.0.1', reload=True)