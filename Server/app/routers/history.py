from fastapi import APIRouter

from app.schemas.response import response_success
from app.utils.history import get_session_history
from app.utils.msg_list import get_ai_response
router = APIRouter(
    prefix='/api/history'
)

@router.get('/',response_model=response_success)
async def history():
    frontend_messages = []
    message = {}
    result = get_session_history("550e8400-e29b-41d4-a716-446655440000")
    for msg in result.messages:
        frontend_messages.append({
            "type": msg.type,   
            "content": msg.content
        })
    response_success.data = frontend_messages
    return response_success

@router.delete('/',response_model=response_success)
async def del_history():
    result = get_session_history("550e8400-e29b-41d4-a716-446655440000")
    result.clear()
    return response_success
