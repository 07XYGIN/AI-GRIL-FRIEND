import os
from dotenv import load_dotenv
from .prompt import SYSTEM_PROMPT
from .tools.message import msg_info
from .tools.search_momery import search_memory_tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from app.schemas.response import ai_response
from .llm_config import llm
load_dotenv()
llm = ChatOpenAI(
    model="qwen-plus",
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=1.9,
    
)
agent = create_agent(
    model=llm,
    system_prompt=SYSTEM_PROMPT,
    response_format=ai_response,
    tools=[msg_info,search_memory_tool],
)