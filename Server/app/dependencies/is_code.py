from fastapi import Header
import logging
async def iscode(code: str | None = Header(default=None, alias="code")):
    logging.info(f"code: {code}")
    return code