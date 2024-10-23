from pydantic import BaseModel
from typing import Any
from fastapi import status


class APIResponse(BaseModel):
    code: int = status.HTTP_200_OK
    msg: str = ""
    data: Any = None

