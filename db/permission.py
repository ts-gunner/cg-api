from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from pydantic import BaseModel


class AuthPermission(Base):
    __tablename__ = "auth_permission"
    permission_id = Column(String(50), primary_key=True, comment="权限代码")
    permission_name = Column(String(50), primary_key=True, comment="权限名称")


# 角色（用户）:权限 -> 多对多
class UserPermission(Base):
    __tablename__ = "user_permission"
    id = Column(Integer, primary_key=True)
    permission_id = Column(String(50), comment="权限代码")
    user_id = Column(String(100), comment="用户id")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class RolePermission(Base):
    __tablename__ = "role_permission"
    id = Column(Integer, primary_key=True)
    permission_id = Column(String(50), comment="权限代码")
    role_id = Column(String(100), comment="角色id")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class AuthPermissionBase(BaseModel):
    permission_id: str
    permission_name: str

    class Config:
        from_attributes = True
