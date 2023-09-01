from my_fastapi.v1.model.todo_model import Todo
from my_fastapi.v1.model.user_model import User
from my_fastapi.v1.utils.database import db


def create_tables() -> None:
    with db:
        db.create_tables([User, Todo])
