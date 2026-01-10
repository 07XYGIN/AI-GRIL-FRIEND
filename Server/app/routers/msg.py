from rich.console import Console
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import AIMessage

# 导入你的组件
from app.core.chain.chain_main import agent
from app.utils.history import get_session_history

console = Console()
router = APIRouter()
def normalize_agent_result(agent_result):
    """
    把各种可能的返回值规范化为 (msgs_list, response_content_str)。
    兼容：dict（带/不带 'output'）、list、字符串、AIMessage 等。
    """
    # dict 情况：优先取 'messages' 和 'output'，其次尝试常见字段名
    if isinstance(agent_result, dict):
        msgs = agent_result.get('messages') or agent_result.get('msgs') or agent_result.get('message') or []
        # 确保 msgs 是 list
        if not isinstance(msgs, list):
            msgs = [msgs]
        response_content = agent_result.get('output') \
                           or agent_result.get('text') \
                           or agent_result.get('response') \
                           or agent_result.get('content') \
                           or ""
        return msgs, response_content

    # list 情况：把 list 当作消息序列
    if isinstance(agent_result, list):
        return agent_result, ""

    # 其它（单个消息、字符串等）
    if hasattr(agent_result, "content"):  # AIMessage-like
        return [agent_result], getattr(agent_result, "content", "") or ""
    # 最后的兜底：把对象 string 化
    return [agent_result], str(agent_result)
@router.websocket("/ws")
async def websocket_sen_msg(websocket: WebSocket):
    session_id = '550e8400-e29b-41d4-a716-446655440000'
    if not session_id:
        await websocket.close(code=1008, reason="Missing session_id")
        return

    await websocket.accept()
    console.print(f"[green]用户 {session_id} 已连接[/green]")

    chain_with_history = RunnableWithMessageHistory(
        agent,
        get_session_history,
        input_messages_key="input",  
        history_messages_key="history",
        # 【关键修改】指定输出消息所在的键，通常是 'messages' 或 'msgs'
        # 如果你的 agent 返回的是包含 messages 列表的字典，这里填 'messages'
        output_messages_key="messages" 
    )
    
    config = {"configurable": {"session_id": session_id}}

    try:
        while True:
            data = await websocket.receive_text()
            
            agent_result = chain_with_history.invoke(
                {"input": data}, 
                config=config
            )
            if isinstance(agent_result, dict):
                msgs = agent_result.get('messages', [])
                response_content = agent_result.get('output', "")
            elif isinstance(agent_result, list):
                msgs = agent_result
                response_content = ""
            else:
                msgs = [agent_result]
                response_content = str(agent_result)
            tool_called = False
                    
            for msg in msgs:
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    for call in msg.tool_calls:
                        if call['name'] == 'ai_response':
                            response_content = call['args'].get("content", "")
                            console.print(f"[yellow]工具调用:[/yellow] {response_content}")
                            tool_called = True

            if not tool_called:
            # 如果之前没有从 tool 调用获取内容
                if not response_content and msgs and isinstance(msgs[-1], AIMessage):
                    response_content = msgs[-1].content
            elif not response_content:
                response_content = "AI 未能生成有效回复"

            await websocket.send_text(response_content)

    except WebSocketDisconnect:
        console.print(f"[red]用户 {session_id} 断开连接[/red]")
    except Exception as e:
        console.print_exception()
        await websocket.send_text(f"Server Error: {str(e)}")