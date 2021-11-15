from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world from fastapi"}


@app.post("/")
async def root_post():
    return {"message": "hello world from fastapi post"}

handler = Mangum(app=app)
