from langchain_postgres import PostgresChatMessageHistory
import psycopg
from app.core.database import SYNC_DATABASE_URL
sync_connection = psycopg.connect(SYNC_DATABASE_URL)
def get_session_history(session_id: str):
    return PostgresChatMessageHistory(
    "chat_history", 
    session_id, 
    sync_connection=sync_connection
    )