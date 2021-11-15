from fastapi import FastAPI
from .users import user_route
from mangum import Mangum

app = FastAPI(
    root_path="/dev/"
)


@app.get("/")
async def root():
    return {"message": "hello world from fastapi"}

app.include_router(user_route, prefix="/users")


@app.post("/")
async def root_post():
    return {"message": "hello world from fastapi post"}

handler = Mangum(app=app)
