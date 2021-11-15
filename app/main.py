from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world from fastapi"}

handler = Mangum(app=app)
