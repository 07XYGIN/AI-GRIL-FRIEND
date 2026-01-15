from fastapi import Header

async def iscode(code: str | None = Header(default=None, alias="code")):
    print(code)
    return code