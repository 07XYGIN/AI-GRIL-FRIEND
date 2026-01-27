import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="qwen3-vl-30b-a3b-thinking",
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    extra_body={"enable_thinking": True},
    streaming=True
)

message = HumanMessage(
    content=[
        {"type": "text", "text": "这道题怎么解答？"},
        {"type": "image_url", "image_url": {"url": "https://img.alicdn.com/imgextra/i1/O1CN01gDEY8M1W114Hi3XcN_!!6000000002727-0-tps-1024-406.jpg"
        }},
    ]
)

result =  llm.invoke([message])

print(result)