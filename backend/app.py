from fastapi import FastAPI
from fastapi.responses import JSONResponse

# routers
from authentication.routes import router as auth_router

# table creations
from db import Base, engine, create_db
from authentication.models import User

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
    create_db()
    print("DB is Connected!")