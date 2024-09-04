from fastapi import FastAPI
from sqladmin import Admin, ModelView

from AcademyApp.config.database import engine

app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


admin.add_view(UserAdmin)
@app.get("/")
async def root():
    return {"message": "Hello Rustam"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
