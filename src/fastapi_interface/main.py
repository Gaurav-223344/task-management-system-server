# fastapi_pydantic/main.py
from fastapi import Depends, FastAPI

app = FastAPI()

# Root endpoint


@app.get("/ping")
def read_root():
    return {"message": "pong"}
