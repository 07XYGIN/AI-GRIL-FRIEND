from pydantic import BaseModel

class request_msg(BaseModel):
    message: str