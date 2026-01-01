from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
import os
from dotenv import load_dotenv
from .prompt import SYSTEM_PROMPT
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
)