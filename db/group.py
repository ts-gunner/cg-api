from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from pydantic import BaseModel


# 用户:组 -> 多对多
class UserGroup(Base):
    __tablename__ = "user_group"
    group_id = Column(String(100), primary_key=True, nullable=False, comment="group id")
    group_name = Column(String(50), comment="组名称")


# 用户:组 -> 多对多
class UserGroupMap(Base):
    __tablename__ = "user_group_map"
    id = Column(Integer, primary_key=True)
    group_id = Column(String(100), nullable=False, comment="group id")
    user_id = Column(String(100), comment="用户id")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class UserGroupBase(BaseModel):
    group_id: str
    group_name: str

    class Config:
        from_attributes = True
