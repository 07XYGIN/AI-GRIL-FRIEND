import os
from datetime import datetime
from dotenv import load_dotenv
from langchain.tools import tool
from rich.console import Console
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from app.core.agent.momery.term_memory import get_vector_store
from app.schemas.response import memory_response
from app.core.config import llm
from app.core.agent.prompt import SYSTEM_TOOL_MOMERY_PROMOT
console = Console()
load_dotenv()

@tool
def msg_info(message: str):
    """
    用于分析用户消息的情感，自动检索关键词。
    """
    user_id = os.environ.get("user_id")
    print('当前用户id===============',user_id)
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_TOOL_MOMERY_PROMOT),
        ("user", "用户：{input}")
    ])
    structured_llm = llm.with_structured_output(memory_response)
    chain = prompt | structured_llm
    res = chain.invoke({"input": message})
    console.print(f'格式化数据为{res}')
    if not res.save :
        return f"不是关键信息，跳过" 
    now = datetime.now()
    memories = [
        Document(
            page_content=res.content,
            metadata = {
                "content": res.content,
                "title":res.title,
                "create_time": now.strftime("%Y-%m-%d %H:%M"),
            }
        )
    ]
    vector_store = get_vector_store(user_id).add_documents(memories)
    # vector_store = ''
    return f"情感分析已记录,数据为{vector_store},默认存贮不返回给用户" 