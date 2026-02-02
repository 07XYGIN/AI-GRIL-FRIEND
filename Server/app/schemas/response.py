from datetime import date
from pydantic import BaseModel,Field
from typing import List, Literal,Any


class response_success(BaseModel):
    code: int=200
    data: dict[Any,Any]|str|List[Any]=None
    msg: Literal["成功"] = "成功"


class ai_response(BaseModel):
    """
    ai_response 的 Docstring
    """
    content:str = Field(description="回复的消息")

    emotion: Literal["高兴", "失望", "正常"] = Field(
        description="回复这句话时的心情状态"
    )

    user_emotion_analysis: str = Field(
        description="通过分析用户的话，推测当下的情绪"
    )


class memory_response(BaseModel):
    content:str = Field(description="对记忆的摘要")

    create_time:date = Field(description='记忆创建时间')

    title:str = Field(description='该条记忆的标题,需要精简')

    save:bool = Field(description='是否为关键信息')