from pydantic import BaseModel
from typing import List, Literal,Any


class response_success(BaseModel):
    code: int=200
    data: dict[Any,Any]=None
    msg: Literal["成功"] = "成功"