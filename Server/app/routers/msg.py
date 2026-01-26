import os 
import random
import asyncio
from fastapi import APIRouter
from rich.console import Console
from fastapi.responses import StreamingResponse
from app.schemas.request import request_msg
from app.core.agent.agent_main import app_with_history
console = Console()
router = APIRouter()

@router.post('/send/sse/')
async def sse_msg(msg:request_msg):
    os.environ["user_id"] = msg.userId
    user_id = msg.userId
    # for i in app_with_history.stream({"input": msg.message},config={"configurable": {"session_id": user_id}}):
    #     print(i)
    result = app_with_history.invoke({"input": msg.message},config={"configurable": {"session_id": user_id}})
    full_text = result.get('output', '')

    async def event_generator():
        i = 0
        while i < len(full_text):
            chunk_size = random.randint(1, 5)
            chunk = full_text[i:i+chunk_size]
            yield f"data: {chunk}\n\n"
            i += chunk_size
            await asyncio.sleep(random.uniform(0.02, 0.1))
        yield "data: [DONE]\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")
    return 0


