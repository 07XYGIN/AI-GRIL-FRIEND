from typing import Any
from fastapi import APIRouter

from app.schemas.response import response_success
from app.utils.history import get_session_history
router = APIRouter(
    prefix='/api/history'
)

@router.delete('/{userId}',response_model=response_success)
async def del_history(userId:Any):
    get_session_history(userId).clear()
    return response_success

@router.get('/{userId}',response_model=response_success)
async def history(userId:Any):
    frontend_messages = []
    result = get_session_history(userId)
    for msg in result.messages:
        frontend_messages.append({
            "type": msg.type,   
            "content": msg.content
        })
    response_success.data = frontend_messages
    return response_success


