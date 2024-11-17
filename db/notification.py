from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from pydantic import BaseModel


# 用户:角色 -> 多对多
class Notification(Base):
    __tablename__ = "notification"
    no_id = Column(String(100), primary_key=True, nullable=False, comment="no_id")
    no_name = Column(String(50), comment="公告名称")
    notify_text = Column(Text, comment="公告内容")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class NotificationBase(BaseModel):
    no_id = Column(String(100), primary_key=True, nullable=False, comment="no_id")
    no_name = Column(String(50), comment="公告名称")
    notify_text = Column(Text, comment="公告内容")
    create_time = Column(DateTime, server_default=func.now())
