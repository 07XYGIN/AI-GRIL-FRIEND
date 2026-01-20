from langchain.tools import tool
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.core.config import llm
from app.core.agent.momery.term_memory import get_vector_store
import os
@tool
def search_memory_tool(query: str) -> str:
    """
    根据用户的输入查询相关的记忆片段。
    
    Args:
        query: 用户的查询内容
        
    Returns:
        基于记忆的回复
    """
    print('='*100)
    user_id = os.environ.get("user_id")
    print('当前用户id===============',user_id)
    vector_store = get_vector_store(user_id)
    # 检索记忆
    print('开始查找记忆')
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    template_text = """
    请基于以下【回忆】来回答男朋友的话。如果回忆里没有相关信息，就自然地聊天，不要捏造事实。

    【回忆片段】：
    {context}
    
    男朋友说：{input}
    
    请以女朋友的身份回复：
    """

    prompt = ChatPromptTemplate.from_template(template_text)
    
    def format_docs(docs):
        """把检索到的 Document 对象列表转为纯字符串"""
        return "\n\n".join([d.page_content for d in docs])
    
    chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    response = chain.invoke(query)
    
    print('#'*100)
    print('检索到的记忆------>', response)
    print('#'*100)
    
    return response