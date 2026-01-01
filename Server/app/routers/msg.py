from app.core.chain.chain_main import agent
from app.schemas.response import response_success
from app.schemas.request import request_msg
from fastapi import APIRouter

from rich.console import Console
console = Console()

router = APIRouter()

@router.post("/msg/send",response_model=response_success)
async def send_message(message: request_msg):
    console.log(f"Received message: {message}")
    response_success.code = 200
    response_success.data = f'hello,{message.message}'
    return response_success