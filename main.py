from typing import Union

from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class User(BaseModel):
    usename:str 
    password: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
def login(user: User):
    if user.usename == "mayur" and user.password == "1234":
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Login successful"})
    else:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Invalid credentials"})