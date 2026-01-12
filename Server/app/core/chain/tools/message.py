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
    用于分析用户消息的情感。
    
    Args:
        user_id: 用户的ID。
        message: 🚨必须完全复制用户当前的输入内容(User Input)，不要修改，不要总结，不要使用默认文本。
    """
    print(f"🛠️ Tool msg_info triggered | User: {user_id} | Message: {message}") 
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
    return "情感分析已记录" 