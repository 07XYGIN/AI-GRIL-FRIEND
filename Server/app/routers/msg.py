import os 
import random
import asyncio
import uuid
import logging
from fastapi import APIRouter, UploadFile
from rich.console import Console
from fastapi.responses import StreamingResponse
from app.schemas.request import request_msg
from app.core.agent.agent_main import app_with_history
console = Console()
router = APIRouter()

uploaded_files = {}

@router.post('/send/sse/')
async def sse_msg(msg:request_msg):
    os.environ["user_id"] = msg.userId
    user_id = msg.userId    
    result = app_with_history.invoke({"input": msg.message},config={"configurable": {"session_id": user_id}})
    logging.info(f'agent返回结果为{result}')
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

@router.post('/uplpad')
async def upload(file:UploadFile):
    console.print(file.content_type,style='red')
    content = await file.read()
    
    file_id = str(uuid.uuid4())
    with open("my_image.pdf", "wb") as f:
    # 3. 写入数据
        f.write(content)
    print(content)
    uploaded_files[file_id] = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "file_id": file_id,
        "content":content
    }
    return 0