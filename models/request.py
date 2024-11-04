from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import status
from models.common import APIResponse
from db.task import TaskCategory, TaskStatus


class AddTaskRequest(BaseModel):
    openid: str
    category: TaskCategory
    content: str
    point: float
    body: Optional[str]


class TaskListRequest(BaseModel):
    openid: str
    status: TaskStatus


class AuditTaskRequest(BaseModel):
    task_id: str
    approve_result: bool  # true 通过， false 不通过
    comment: str

