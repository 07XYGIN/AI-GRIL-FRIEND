from app.core.chain.chain_main import agent
from app.schemas.response import response_success
from app.schemas.request import request_msg
from app.core.chain.chain_main import llm
from fastapi import APIRouter

from rich.console import Console
console = Console()

router = APIRouter()

@router.post("/msg/send")
async def send_message(message: request_msg):
    console.log(f"Received message: {message}")
    prompt = agent.invoke({"messages": [{"role": "user", "content": message.message}]})
    promptlist = prompt['messages']
    console.log(f"Generated response: {promptlist}")
    return promptlist