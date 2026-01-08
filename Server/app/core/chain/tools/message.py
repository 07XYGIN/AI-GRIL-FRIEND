from langchain.tools import tool
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
llm = ChatOpenAI(
    model="qwen-plus",
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=1.9,
)
@tool
def msg_info(user_id: str, message: str):
    """
        对用户发送的信息进行总结,不作为回复消息
    Args:
        user_id: 用户唯一标识
        message: 用户发送的文本信息

    Returns:
        对输入信息的总结
    """
    print("使用了msg_info")
    print('用户输入的信息:',message)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "'你是用户的虚拟女友，温柔、关心用户，回复要贴心和亲切。'"),
        ("user", "请把下面的话总结成一句完整且温柔的句子，用女朋友的语气回复我,{input}")
    ])
    chain = prompt | llm | StrOutputParser()

    res = chain.invoke({"input":message})
    print(res)
    return res  