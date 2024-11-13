from typing import Optional
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


class RewardsBalanceBase(BaseModel):
    user_id: str
    total_points: float
    used_points: float

    class Config:
        from_attributes = True


class MarketGoods(Base):
    __tablename__ = "market_goods"
    id = Column(Integer, primary_key=True)
    good_id = Column(String(100), nullable=False, comment="good ID")
    good_name = Column(String(100), nullable=False, comment="商品名称")
    description = Column(String(255), comment="商品描述")
    point = Column(DECIMAL(10, 2), comment="兑换需要的积分")
    display_img_path = Column(Text, comment="展示出来的商品图片路径")
    remark = Column(String(255), comment="备注")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class MarketGoodsBase(BaseModel):
    good_id: str
    good_name: str
    description: str
    point: float
    display_img_path: str
    remark: Optional[str]

    class Config:
        from_attributes = True
