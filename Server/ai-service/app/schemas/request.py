from typing import Any
from pydantic import BaseModel

class request_msg(BaseModel):
    message: str
    userId:str


class register_from(BaseModel):
    userName:str
    password:str
    code:str

class login_from(BaseModel):
    userName:str
    password:str
    code:str
