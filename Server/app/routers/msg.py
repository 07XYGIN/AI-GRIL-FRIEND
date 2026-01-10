from app.core.chain.chain_main import agent
from fastapi import APIRouter,WebSocket,WebSocketDisconnect
from rich.console import Console
console = Console()
router = APIRouter()
@router.websocket("/ws")
async def websocket_sen_msg(websocket: WebSocket):
    await websocket.accept() 
    try:
        while True: 
            data = await websocket.receive_text()
            agent_result = agent.invoke({"messages": [{"role": "user", "content": data}]})
            console.print(agent_result)
            promptlist = agent_result['messages']
            console.print(promptlist)
            frontend_response = {}
            for msg in promptlist:
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    for call in msg.tool_calls:
                        console.print(call)
                        if call['name'] == 'ai_response':
                            console.print(call)
                            frontend_response['content'] = call['args'].get("content", "")
                            
            await websocket.send_text(f"{frontend_response["content"]}") 
    except WebSocketDisconnect:
        print("Client disconnected")