import uvicorn
import json
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
app = FastAPI()

class req_body(BaseModel):
    userId : str
    msg : str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/send/sse/')
async def sse_stream():
    async def event_generator():
        count = 0
        while True:
            if count == 5:
                return
            data = {"message": f"Event {count}", "count": count}
            yield f"data: {json.dumps(data)}\n\n"
            
            count += 1
            await asyncio.sleep(1)
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

if __name__ == '__main__':
    uvicorn.run(
        "serv:app",
        port=8000,
        reload=True,
    )