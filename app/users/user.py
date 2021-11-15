from fastapi import APIRouter
from datetime import datetime

user_route = APIRouter()


@user_route.get("/")
def get_user():
    return {"name": "qiushi",
            "last_login": datetime(2021, 11, 14)}
