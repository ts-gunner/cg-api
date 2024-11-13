
from pydantic import BaseModel, field_validator,  Field
from typing import Optional, List
from fastapi import status

from db.task import TaskCategory, TaskStatus


class AddTaskRequest(BaseModel):
    task_id: str
    openid: str
    category: TaskCategory
    content: str
    point: float
    body: Optional[str]
    upload_list: List[str]


class TaskListRequest(BaseModel):
    openid: str
    status: TaskStatus


class AuditTaskRequest(BaseModel):
    task_id: str
    approve_result: bool  # true 通过， false 不通过
    comment: str


class WorkerRecordRequest(BaseModel):
    role_id: str
    status: str


