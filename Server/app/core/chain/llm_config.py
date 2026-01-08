import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
llm = ChatOpenAI(
    model="qwen-plus",
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=1.9,
)