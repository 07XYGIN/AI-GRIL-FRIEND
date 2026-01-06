from fastapi import APIRouter,Depends
from rich.console import Console
from app.core.exceptions import UnicornException
from app.schemas.response import response_success
from app.schemas.request import login_from
from app.utils.verify import get_password_hash
from app.core.database import get_db
from app.model.User import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from fastapi import HTTPException
console = Console()

router = APIRouter(
    prefix='/api'
)

@router.post('/register',response_model=response_success)
async def register(login:login_from,db: AsyncSession = Depends(get_db)):
    user = select(User.user_name).where(User.user_name == login.userName)
    result = await db.execute(user)
    isUser = result.scalar_one_or_none()
    # 不等于None说明表中已经存在
    if isUser is not None:
        raise UnicornException(name=login.userName)
    password = get_password_hash(login.password)
    register_from =  User(
        user_name = login.userName,
        psd=password
    )
    db.add(register_from)   
    await db.commit()
    await db.refresh(register_from)
    return response_success
