from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

# MODEL
class User(BaseModel):
    id: int
    name: str
    age: int


# CREATE
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "data": user}


# READ ALL
@app.get("/users")
def get_users():
    return users


# READ ONE
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# UPDATE
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = updated_user
            return {"message": "User updated", "data": updated_user}
    raise HTTPException(status_code=404, detail="User not found")


# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted = users.pop(i)
            return {"message": "User deleted", "data": deleted}
    raise HTTPException(status_code=404, detail="User not found")