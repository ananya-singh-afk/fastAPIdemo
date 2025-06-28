from typing import List
from uuid import UUID, uuid4
from fastapi import Body, FastAPI, HTTPException
from models import Gender, Role, User, UpdateUser

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

@app.delete("/api/users/{user_id}") #{user_id} is a path parameter/variable 
async def delete_user(user_id: UUID):
    for user in db:
        # Check if the user with the given ID exists
        # If it does, we break the loop
        # If it doesn't, we continue to the next user
        # This is a more efficient way to find the user
        # and avoids unnecessary iterations
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
        raise HTTPException(
            status_code=404,
            detail=f"User not found: {user_id} - User does not exist"
        )
    
@app.put("/api/users/{user_id}") #{user_id} is a path parameter/variable
async def update_user(user_id: UUID, user: UpdateUser = Body(...)):
    for index, existing_user in enumerate(db):
        if existing_user.id == user_id and user.first_name and user.last_name and user.gender and user.roles is not None:
            db[index] = user
            return {"message": "User updated successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"User not found: {user_id} - User does not exist"
    )