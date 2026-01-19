import os
import json
import asyncio
from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from rich.console import Console
from app.core.chain.chain_main import app_with_history

console = Console()
router = APIRouter()

# 定义请求体模型，用于接收前端发送的消息
class ChatRequest(BaseModel):
    message: str

@router.post("/sse/{userId}")
async def sse_chat_endpoint(userId: str, request: ChatRequest):
    """
    SSE 端点：接收 POST 请求，流式返回 AI 响应
    """
    user_message = request.message
    
    # 警告：在 async 环境中直接修改 os.environ 是非线程安全的，
    # 如果有并发请求，userId 会被覆盖。建议仅依赖下面的 session_id 配置。
    os.environ["user_id"] = userId 
    for token in app_with_history.stream({"input": user_message},config={"configurable": {"session_id": userId}}):
        console.log(token)
    async def event_generator():
            # 这里的逻辑与原 WebSocket 保持一致
            # 注意：如果 app_with_history 支持 .ainvoke (异步调用)，建议使用 await app_with_history.ainvoke(...)
            #以此避免阻塞服务器的主线程
            # agent_result = await asyncio.to_thread(
            #     app_with_history.ainvoke,
            #     {"input": user_message},
            #     config={"configurable": {"session_id": userId}}
            # )

            # --- 原有结果解析逻辑 ---
            # if 'output' not in agent_result:
            #     if 'structured_response' in agent_result:
            #         structured = agent_result['structured_response']
            #         if hasattr(structured, 'content'):
            #             agent_result['output'] = structured.content
            #     if 'output' not in agent_result:
            #         agent_result['output'] = "无法解析回复内容"
            
            # promptlist = agent_result.get('messages', [])
            # frontend_response_content = ""

            # # 优先查找 tool_calls 中的 ai_response
            # found_tool_response = False
            # for msg in promptlist:
            #     if hasattr(msg, "tool_calls") and msg.tool_calls:
            #         for call in msg.tool_calls:
            #             if call['name'] == 'ai_response':
            #                 frontend_response_content = call['args'].get("content", "")
            #                 found_tool_response = True
            
            # # 如果没找到 tool_calls，通常使用 agent_result['output'] 作为兜底
            # if not found_tool_response:
            #     frontend_response_content = agent_result['output']

            # --- SSE 数据格式化 ---
            # SSE 格式要求以 "data: " 开头，以 "\n\n" 结尾
            # 为了前端方便解析，通常将内容处理一下（例如处理换行符）
            # 这里直接发送纯文本，也可以 json.dumps 包装
            # yield f"data: {frontend_response_content}\n\n"
            
            # 发送结束信号（可选，视前端实现而定，通常流结束由连接关闭表示）
            # yield "event: close\ndata: [DONE]\n\n"

        # except Exception as e:
        #     console.print_exception()
        #     yield f"data: Error: {str(e)}\n\n"

    # 返回 StreamingResponse，媒体类型必须为 text/event-stream
        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no" # 防止 Nginx 缓存流数据
            }
        )