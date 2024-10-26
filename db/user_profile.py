from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional


class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True)
    openid = Column(String(100), primary_key=True, nullable=False, comment="微信提供当前小程序的openid，标识个人id")
    unionid = Column(String(100), comment="微信提供多平台的unionid，标识同一用户在不同应用的id")
    nickname = Column(String(100), comment="用户昵称")
    phone_number = Column(String(50), comment="手机号码")
    avatar_url = Column(Text, comment="头像地址")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class UserProfileBase(BaseModel):
    openid: str
    unionid: Optional[str]
    nickname: Optional[str]
    phone_number: Optional[str]
    avatar_url: Optional[str]

    class Config:
        from_attributes = True
