from fastapi import FastAPI

from my_fastapi.v1.model.user_model import User
from my_fastapi.v1.routers.user_router import router as user_router
from my_fastapi.v1.utils.database import db as connection

app = FastAPI(
    title="My first API",
    description="My first endpoints",
    version="1.0.0",
)
app.include_router(user_router)


@app.on_event("startup")
def startup() -> None:
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])


@app.on_event("shutdown")
def shutdown() -> None:
    if not connection.is_closed():
        connection.close()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
