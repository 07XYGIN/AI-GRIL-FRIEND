from fastapi import APIRouter,Depends
from rich.console import Console
from app.core.exceptions import UnicornException,loginerr,LoginException
from app.schemas.response import response_success
from app.schemas.request import login_from,register_from
from app.utils.verify import get_password_hash,verify_password
from app.core.database import get_db
from app.model.User import User
from app.model.code import BetaCode
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
console = Console()

router = APIRouter(
    prefix='/api'
)

@router.post('/register',response_model=response_success)
async def register(login:register_from,db: AsyncSession = Depends(get_db)):
    user = select(User.user_name).where(User.user_name == login.userName)
    result = await db.execute(user)
    isUser = result.scalar_one_or_none()
    # 不等于None说明表中已经存在
    if isUser is not None:
        raise UnicornException(name=login.userName)
    password = get_password_hash(login.password)
    register_from =  User(
        user_name = login.userName,
        psd=password,
        code=login.code
    )
    db.add(register_from)   
    await db.commit()
    await db.refresh(register_from)
    return response_success


@router.post('/login',response_model=response_success)
async def login(login:login_from,db: AsyncSession = Depends(get_db)):
    console.log(login)
    user = (
        select(User.psd,User.code)
        .where(User.user_name == login.userName)
    )
    result = await db.execute(user)
    row = result.one_or_none()
    if row is None:
        raise LoginException("用户不存在")
    # 解包元组
    console.log(row)
    base_psd, code_info = row
    console.log(code_info)
    console.log(login.code)
    if not verify_password(login.password, base_psd):
        raise LoginException("密码错误")
    if code_info is None or login.code != code_info:
        raise LoginException("邀请码错误")
    response_success.data = code_info
    return response_success