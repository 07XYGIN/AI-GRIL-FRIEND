import os 
import random
import asyncio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.core.chain.chain_main import app_with_history
from rich.console import Console
console = Console()
router = APIRouter()

@router.get('/send/sse/')
async def sse_msg(msg:str):
    os.environ["user_id"] = 'd86cebdb-a1d9-426c-a84f-6db31cb4200a'
    user_id = 'd86cebdb-a1d9-426c-a84f-6db31cb4200a'
    result = app_with_history.invoke({"input": msg},config={"configurable": {"session_id": user_id}})
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