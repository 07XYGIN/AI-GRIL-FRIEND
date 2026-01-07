from pydantic import BaseModel

class request_msg(BaseModel):
    message: str


class register_from(BaseModel):
    userName:str
    password:str

class login_from(BaseModel):
    userName:str
    password:str
    code:str
