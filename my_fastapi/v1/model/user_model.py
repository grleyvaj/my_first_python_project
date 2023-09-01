import peewee

from my_fastapi.v1.utils.database import db


class User(peewee.Model):
    username = peewee.CharField(unique=True, index=True, max_length=50)
    email = peewee.CharField(unique=True, index=True, max_length=50, null=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        database = db
        table_name = "users"
