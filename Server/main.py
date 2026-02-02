import uvicorn
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.routers import msg
from app.routers import login
from app.routers import history
from app.routers import user
from app.core.exceptions import unicorn_exception_handler,UnicornException,validation_exception_handler,loginerr,LoginException
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info('程序启动')

    yield 

    logging.info('程序关闭')

def create_app():
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        max_age=86400
    )
    routers:list[any,any] = [msg.router,login.router,history.router,user.router]
    for router in routers:
        app.include_router(router)

    exception_handlers = [
        (UnicornException, unicorn_exception_handler),
        (LoginException, loginerr),
        (RequestValidationError, validation_exception_handler)
        ]
    for exc_type, handler in exception_handlers:
        app.add_exception_handler(exc_type, handler)
    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True,
    )

