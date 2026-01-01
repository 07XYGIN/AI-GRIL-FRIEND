from pydantic import BaseModel
from typing import Literal


class response_success(BaseModel):
    code: int
    data: str
    msg: Literal["成功"] = "成功"
    role: Literal["assistant"] = "assistant"