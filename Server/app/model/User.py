from sqlalchemy import TEXT, TIMESTAMP, Boolean, String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.sql import func
from app.core.database import Base 
class User(Base):
    __tablename__ = "girlfriend_configs" 

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False)
    personality: Mapped[str] = mapped_column(TEXT, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), 
        server_default=func.now(),
        nullable=False
    )