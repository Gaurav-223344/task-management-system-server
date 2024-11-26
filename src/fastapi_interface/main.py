# fastapi_pydantic/main.py
from fastapi import Depends, FastAPI
from fastapi.concurrency import asynccontextmanager

from .services import database_setup

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database_setup()
    yield  
    print("Cleaning up resources...")

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
def read_root():
    return {"message": "pong"}
