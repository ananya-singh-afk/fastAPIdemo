from typing import List
from uuid import UUID, uuid4
from fastapi import Body, FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("91f19956-6097-4f7f-888e-072e08ac5c16"), #making the uuid fixed by defining it like this
        first_name="Ananya",last_name="Singh",
        gender= Gender.female,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(), #generating uuid each time 
        first_name="Kiran",last_name="Singh",
        gender= Gender.female,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hey": "Today we learn FastAPI, tomorrow we take on the world!"}

@app.get("/api/users")
async def fetch_users():
    return db;

@app.post("/api/users")
async def register_user(user: User = Body(...)):
    db.append(user)
    return {"id": user.id}
#User is the entity and user is what we receive from the request body
