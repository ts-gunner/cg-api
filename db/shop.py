from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, DECIMAL
from sqlalchemy.sql import func, text
from pydantic import BaseModel


# 积分表
class RewardsBalance(Base):
    __tablename__ = "rewards_balance"
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), comment="用户id")
    total_points = Column(DECIMAL(10, 2), default=0, server_default=text("0"), comment="总积分 | 剩余积分")
    used_points = Column(DECIMAL(10, 2), default=0, server_default=text("0"), comment="已用积分")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())
