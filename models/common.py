from email.policy import default

from pydantic import BaseModel, Field
from typing import Any, Optional, List
from fastapi import status
from db.role import UserRoleBase
from db.group import UserGroupBase


class APIResponse(BaseModel):
    code: int = status.HTTP_200_OK
    msg: str = ""
    data: Any = None


class SettingBase(BaseModel):
    store_path: str = Field(default="", description="对象储存路径")
    bucket_store_type: str = Field(default="local", description="对象存储类型")
    user_store_path: str = Field(default="", description="用户附件储存位置")
    bucket_name: str = Field(default="", description="仓库名称")
    app_secret: str = Field(default="", description="app key")


class TokenData(BaseModel):
    user_id: str = ""
    groups: List[UserGroupBase] = []
    roles: List[UserRoleBase] = []
    permissions: List[str] = []
