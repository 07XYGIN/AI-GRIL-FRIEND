# app/utils/history.py
from langchain_community.chat_message_histories import PostgresChatMessageHistory
import logging

# 配置你的 PG 连接字符串
# 格式: postgresql://用户名:密码@地址:端口/数据库名
DB_CONNECTION = "postgresql://postgres:123456@localhost:5432/aigirl"
from langchain_core.messages import messages_to_dict
def get_session_history(session_id: str):
    """
    工厂函数：根据 session_id 返回对应的 PG 历史记录对象。
    如果没有表，LangChain 会自动创建表（默认表名 message_store）。
    """
    return PostgresChatMessageHistory(
        connection_string=DB_CONNECTION,
        session_id=session_id,
        table_name="chat_history"  # 自定义表名
    )

history_obj = get_session_history("user_123_session")

messages = history_obj.messages

raw_data = messages_to_dict(messages)

print(raw_data)