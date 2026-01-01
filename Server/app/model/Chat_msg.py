from sqlalchemy import ForeignKey, String, Integer, Text,TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base 
from pgvector.sqlalchemy import Vector
from datetime import datetime
from sqlalchemy.sql import func 
from .User import User
class Chat_msg(Base):
    __tablename__ = "chat_msg"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer,ForeignKey(User.id), nullable=False, index=True)
    chat_message:Mapped[str] = mapped_column(Text, nullable=False)
    created_at:Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False,default=datetime.now)
    role:Mapped[str] = mapped_column(String(20), nullable=False)
    vectors:Mapped[list[float]] = mapped_column(Vector(768), nullable=True)