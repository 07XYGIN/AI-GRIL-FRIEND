from sqlalchemy import ForeignKey, String, Integer, Text,TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base 
from pgvector.sqlalchemy import Vector
from .User import User
from .Chat_msg import Chat_msg
class Chat_msg(Base):
    __tablename__ = "memory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer,ForeignKey(User.id), nullable=False, index=True)
    source_msg_id:Mapped[list[float]] = mapped_column(Integer,ForeignKey(Chat_msg.id), nullable=False, index=True)
    content:Mapped[str] = mapped_column(Text, nullable=True)
    memory_type:Mapped[str] = mapped_column(String(20), nullable=True)
    embedding:Mapped[list[float]] = mapped_column(Vector(768), nullable=True)