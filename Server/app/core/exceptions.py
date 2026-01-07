from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

class LoginException(Exception):
    def __init__(self, name: str):
        self.name = name

async def unicorn_exception_handler(
    request: Request,
    exc: UnicornException
):
    return JSONResponse(
        status_code=500,
        content={
            "message": f" {exc.name} 已存在",
            "code": 500
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "code": 422,
            "message": "不合法的参数",
        }
    )

async def loginerr(request: Request,exc: LoginException):
    return JSONResponse(
            status_code=500,
            content={
                "message": f"用户名或密码错误",
                "code": 500
            }
        )