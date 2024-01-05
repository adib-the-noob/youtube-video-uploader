from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# routers
from authentication.routes import router as auth_router
from workspace.routes import router as workspace_router

# table creations
from db import Base, engine, create_db

Base.metadata.create_all(bind=engine)

app = FastAPI() 

app.mount('/media', StaticFiles(directory='media'), name='media')

app.include_router(auth_router)
app.include_router(workspace_router) 

@app.on_event('startup')
async def startup_event():
    create_db()
    print("DB is Connected!")