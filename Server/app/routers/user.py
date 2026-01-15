from fastapi import APIRouter,Header,Depends
from typing import Optional
from rich.console import Console
from app.core.database import get_db
from app.schemas.response import response_success
from app.model.User import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

console = Console()
router = APIRouter(
    prefix="/api/user"
)

@router.get('/info',response_model=response_success)
async def get_user_info(db: AsyncSession = Depends(get_db),code:Optional[str] = Header(None)):
    user = select(User.create_at,User.id,User.user_name).where(User.code == code)
    result = await db.execute(user)
    row = result.one_or_none()
    createTime,userId,username = row
    success = {
        "createTime":createTime,
        "userId":userId,
        "userName":username
    }
    response_success.data = success
    return response_success
