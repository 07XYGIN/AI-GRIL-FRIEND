from app.core.chain.chain_main import app_with_history
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
            print('data=======',data)
            if data == "ping":
                await websocket.send_text("pong")
                continue
            # agent_result = app_with_history.invoke({"messages": [{"role": "user", "content": data}]})
            agent_result = app_with_history.invoke(
                {"input": data}, 
                config={"configurable": {"session_id": "550e8400-e29b-41d4-a716-446655440000"}}
            )
            if 'output' not in agent_result:
                if 'structured_response' in agent_result:
                    structured = agent_result['structured_response']
                    if hasattr(structured, 'content'):
                        agent_result['output'] = structured.content
                if 'output' not in agent_result:
                    agent_result['output'] = "无法解析回复内容"
            promptlist = agent_result['messages']
            frontend_response = {}
            for msg in promptlist:
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    for call in msg.tool_calls:
                        if call['name'] == 'ai_response':
                            frontend_response['content'] = call['args'].get("content", "")
            await websocket.send_text(f"{frontend_response["content"]}") 
    except WebSocketDisconnect:
        print("Client disconnected")