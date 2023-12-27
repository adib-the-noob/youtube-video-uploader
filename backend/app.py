from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

# routers
from authentication.routes import router as auth_router


# table creations
from db import Base, engine
from authentication.models import User
from app import create_db

Base.metadata.create_all(bind=engine)

app = FastAPI() 
app.include_router(auth_router)
 

@app.get('/Bro')
async def root():
    return JSONResponse({
        "message" : "welcome Bro!"
    })  


@app.on_event('startup')
async def startup_event():
    await create_db()