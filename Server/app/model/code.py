from sqlalchemy import Column, String, Date, ForeignKey, Index, func,text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

import uuid


class BetaCode(Base):
    __tablename__ = 'beta_code'
    __table_args__ = (
        Index('idx_beta_code_unused', 'user_by_id'),
    )
    
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    create_at: Mapped[str] = mapped_column(
        Date,
        server_default=text("(CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Shanghai')")
    )
    user_by_id = Column(UUID(as_uuid=True), ForeignKey('login_user.id'))
    

