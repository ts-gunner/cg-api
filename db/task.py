from typing import Optional
from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, DECIMAL
from sqlalchemy.sql import func
from pydantic import BaseModel, field_validator
from enum import Enum
import datetime


class TaskStatus(str, Enum):
    CREATED = "created"  # 任务刚创建
    INPROGRESS = "in progress"  # 任务进行中
    REVIEW = "review"  # 任务待检查
    APPROVED = "approved"  # 任务审核通过
    FAILED = "failed"  # 任务审核失败
    DEPRECATED = "deprecated"  # 任务作废
    ALL = "all"


class TaskCategory(str, Enum):
    SPORT = "sport"
    STUDY = "study"
    HOUSEWORK = "housework"
    OTHER = "other"


class TaskInfo(Base):
    __tablename__ = "task_info"
    task_id = Column(String(100), primary_key=True, comment="task ID")
    user_id = Column(String(100), comment="user id")
    category = Column(String(30), nullable=False, comment="任务种类")
    point = Column(DECIMAL(10, 2), comment="任务分数")
    status = Column(String(30), nullable=False, comment="任务状态")
    content = Column(String(255), nullable=False, comment="任务内容")
    attach_list = Column(Text, comment="证明")
    body = Column(Text, comment="任务其他内容json")
    remark = Column(String(255), comment="审核备注")
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now())


class TaskInfoBase(BaseModel):
    task_id: str
    category: str
    point: float
    status: str
    content: str
    body: str
    attach_list: str
    create_time: str
    remark: Optional[str]

    @field_validator("create_time", mode="before")
    @classmethod
    def switch_datetime_to_str(cls, v):
        if isinstance(v, datetime.datetime):
            return v.strftime("%Y-%m-%d %H:%M:%S")
        return v

    class Config:
        from_attributes = True
