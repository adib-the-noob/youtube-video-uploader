from fastapi import FastAPI
from fastapi.responses import JSONResponse

from authentication.models import User
from db import db_dependency

app = FastAPI()

@app.get('/')
async def root():
    return JSONResponse({
        "message" : "welcome Bro!"
    })  

@app.get('/add')
async def add_user(db: db_dependency):
    user1 = User(
        full_name="ADIB",
        email="adib"
    ).save(
        db
    )
    return JSONResponse({
        "message" : "DOne"        
    })