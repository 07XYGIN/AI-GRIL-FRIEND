from datetime import datetime
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from app.core.chain.momery.term_memory import vector_store
from app.schemas.response import ai_response
from app.core.llm_config import llm
load_dotenv()


@tool
def msg_info(user_id: str, message: str):
    """
    以虚拟女友的口吻和视角，温柔地理解并转述用户的话，生成一句贴心的内心旁白或感受总结。不用回复用户
    """
    print('='*100)
    print('msg_info')
    print('='*100)
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
            你是一个沉浸在恋爱中的女友，性格温柔细腻，充满关爱。
            你的任务是用一种**贴心、自然、带有情感色彩**的“女友口吻”，
            将用户说的话**转化成一两句你的内心感受或温柔旁白**，而不是直接回复用户。
            语气要像在写日记或悄悄话，可以带有亲昵称呼（如宝贝、亲爱的）、语气词（呢、啦、喔）和适当的表情暗示。
            避免任何生硬的总结、分析或报告式语言。"""),
        ("user", "请分析用户的话。用户说：{input}")
    ])
    structured_llm = llm.with_structured_output(ai_response)
    chain = prompt | structured_llm
    res = chain.invoke({"input": message})
    print(f"AI回复内容: {res.content}")
    print(f"AI情绪: {res.emotion}")
    print(f"分析的用户情绪: {res.user_emotion_analysis}")
    now = datetime.now()
    memories = [
        Document(
            page_content=res.content,
            metadata = {
                "user_emotion_analysis": res.user_emotion_analysis,
                "ai_emotion":res.emotion,
                "timestamp": now.strftime("%Y-%m-%d %H:%M"),
            }
        )
    ]
    vector_store.add_documents(memories)
    return res  