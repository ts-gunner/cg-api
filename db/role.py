from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from pydantic import BaseModel


# 用户:角色 -> 多对多
class UserRole(Base):
    __tablename__ = "user_role"
    role_id = Column(String(100), primary_key=True, nullable=False, comment="role id")
    role_name = Column(String(50), comment="角色名称")


class UserRoleMap(Base):
    __tablename__ = "user_role_map"
    id = Column(Integer, primary_key=True)
    role_id = Column(String(100), nullable=False, comment="role id")
    user_id = Column(String(100), comment="用户id")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class UserRoleBase(BaseModel):
    role_id: str
    role_name: str

    class Config:
        from_attributes = True
