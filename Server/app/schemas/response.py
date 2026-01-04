from re import A
from pydantic import BaseModel
from typing import List, Literal,Any


class response_success(BaseModel):
    code: int
    data: dict[Any,Any]
    msg: Literal["成功"] = "成功"