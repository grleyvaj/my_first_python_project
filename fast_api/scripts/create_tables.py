from fast_api.model.todo_model import Todo
from fast_api.model.user_model import User
from fast_api.utils.database import db


def create_tables() -> None:
    with db:
        db.create_tables([User, Todo])
