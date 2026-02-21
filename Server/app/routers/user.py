from typing import Optional
from fastapi import APIRouter,Header,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.schemas.response import response_success
from app.model.User import User
from app.core.exceptions import UnicornException
from app.core.agent.momery.term_memory import get_vector_store


router = APIRouter(
    prefix="/api/user"
)

@router.get('/info',response_model=response_success)
async def get_user_info(db: AsyncSession = Depends(get_db),code:Optional[str] = Header(None)):
    user = select(User.create_at,User.id,User.user_name).where(User.code == code)
    result = await db.execute(user)
    row = result.one_or_none()
    if row is None:
        raise UnicornException(name="用户不存在",status_code=404)
    createTime,userId,username = row
    success = {
        "createTime":createTime,
        "userId":userId,
        "userName":username
    }
    response_success.data = success
    return response_success

@router.delete('/delMemory/{user_id}',response_model=response_success)
async def del_mem(user_id:str):
    vector_store = get_vector_store(user_id)
    results = vector_store.similarity_search(f"user_id:{user_id}", k=1000)
    vector_ids = [doc.id for doc in results] 
    vector_store.delete(vector_ids) 
    return response_success

@router.get('/memoryList/',response_model=response_success)
async def get_memory_list(user_id:str):
    vector_store = get_vector_store(user_id)
    results = vector_store.similarity_search(f"user_id:{user_id}", k=50)
    memory_list = [doc for doc in results] 
    response_success.data = memory_list
    return response_success


@router.delete('/delSingleItemMomery/{user_id}/{del_id}',response_model=response_success)
async def del_single_data(user_id:str,del_id:str):
    vector_store = get_vector_store(user_id)
    vector_store.delete([del_id])
    return response_success