from pydantic import BaseModel
from fastapi import status
from typing import Any

class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class HttpResponse(BaseModel):
    code: int = status.HTTP_200_OK
    msg: str = ""
    data: Any = None
