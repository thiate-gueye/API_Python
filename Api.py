# -*- coding: utf-8 -*-

from fastapi import FastAPI,HTTPException
import uvicorn
from typing import List
from pydantic import BaseModel


app = FastAPI()
users_list = []

class UserIn(BaseModel):
    nom : str
    prenom : str
    age : int
    
 # get , post , put , delete
 # get
@app.get("/users", response_model=List[UserIn])
async def get_all():
    return users_list


# get by id
@app.get("/users/user_id",response_model=UserIn)
async def user_number(user_id : int):
    try:
         return users_list[user_id]
    except:
        raise HTTPException(status=404)


# post
@app.post("/users",response_model=UserIn)
async def save(user : UserIn):
    users_list.append(user)
    return user

# put
@app.put("/users",response_model=UserIn)
async def update(new_user : UserIn, user_id : int):
    try:
        users_list[user_id] = new_user
        return new_user
    except:
        raise HTTPException(status=404)

# delete
@app.delete("/users")
async def delete(user_id : int):
    try:
        users_list.pop(user_id)
        return "utilisateur d'identifiant "+str(user_id)+" supptimé avec suuces"
    except:
        raise HTTPException(status=404)


