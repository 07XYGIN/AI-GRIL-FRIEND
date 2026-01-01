from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.chain.chain_main import agent
from app.routers import msg
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):

    print(f'程序启动成功')

    yield 

    print("关闭成功")
app = FastAPI(lifespan=lifespan)
app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        max_age=86400
)
app.include_router(msg.router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True,
    )

