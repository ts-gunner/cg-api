import json
from typing import Optional
from fastapi import status
from sqlalchemy.orm import Session
from db.task import TaskCategory, TaskInfo, TaskStatus, TaskInfoBase
from db.shop import RewardsBalance
from models.common import APIResponse
from utils.logger import LoguruLogger
from models.request import AddTaskRequest, TaskListRequest
from utils.encrypt import create_object_id
from utils.math import round_2
from decimal import Decimal

class TaskDataManager:
    def __init__(self, db: Session):
        self.db = db

    def add_task(
            self,
            openid: str, category: TaskCategory, content: str, point: float,
            body: Optional[str] = "", task_status: str = TaskStatus.CREATED.value
    ):
        task_id = create_object_id()
        tk = TaskInfo()
        tk.task_id = task_id
        tk.user_id = openid
        tk.category = category.value
        tk.content = content
        tk.point = round_2(point)
        tk.status = task_status
        tk.body = body
        tk.attach_list = json.dumps([])
        self.db.add(tk)
        return task_id

    def get_task_object(self, task_id: str) -> TaskInfo:
        return self.db.query(TaskInfo).filter(TaskInfo.task_id == task_id).first()

    def get_task_list(self, openid: str, state: str = TaskStatus.CREATED.value):
        task_list = self.db.query(TaskInfo).filter(
            TaskInfo.user_id == openid, TaskInfo.status == state).order_by(TaskInfo.create_time.desc()).all()
        return [TaskInfoBase.model_validate(task) for task in task_list]

    def get_balance_object(self, user_id: str) -> RewardsBalance:
        balance = self.db.query(RewardsBalance).filter(RewardsBalance.user_id == user_id).first()
        if not balance:
            balance = RewardsBalance(user_id=user_id)
            self.db.add(balance)
            self.db.commit()
        return balance


class TaskService:
    def __init__(self, db: Session):
        self.db = db
        self._logger = LoguruLogger.get_logger()
        self._dm = TaskDataManager(db)

    def add_task(self, request: AddTaskRequest):
        task_id = self._dm.add_task(request.openid, request.category, request.content, request.point, request.body, TaskStatus.REVIEW.value)
        self.db.commit()
        return APIResponse(data=task_id)

    def bind_attachment_to_task(self, task_id: str, remote_url: str):
        obj = self._dm.get_task_object(task_id)
        if not obj:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST)
        attach_list = json.loads(obj.attach_list)
        attach_list.append(remote_url)
        obj.attach_list = json.dumps(attach_list)
        self.db.commit()
        return APIResponse()

    def get_task_list(self, request: TaskListRequest):
        return APIResponse(data=self._dm.get_task_list(request.openid, request.status.value))

    def get_task(self, task_id: str):
        task_obj = self._dm.get_task_object(task_id)
        if task_obj:
            return APIResponse(data=TaskInfoBase.model_validate(task_obj))
        else:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, msg="找不到该记录")

    def audit_task_approval(self, task_id: str, approval_result: bool, comment: str):
        """
        任务的审核逻辑：
        1. 如果任务处于review状态，则可以审核通过或者不通过 （可删除）
        2. 如果任务处于approved状态， 则不可以再次审核， （不可删除）
        3. 如果任务处于failed状态，则可以回退到review， （不可删除）
        """
        task_object = self._dm.get_task_object(task_id)
        if not task_object:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, msg="任务记录不存在，请检查后再审核")

        if task_object.status == TaskStatus.REVIEW.value:
            task_object.status = TaskStatus.APPROVED.value if approval_result else TaskStatus.FAILED.value
            task_object.remark = comment

            # 计算积分
            self.calculate_user_points(task_object.user_id, task_object.point)
            self.db.commit()
            return APIResponse(msg="审核成功")
        elif task_object.status == TaskStatus.APPROVED.value:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, msg="审核失败， 原因：该任务已是审核通过状态，不能重复审核")
        elif task_object.status == TaskStatus.FAILED.value:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, msg="审核失败， 原因：该任务是审核不通过状态，不能审核，如需审核，请回退")
        else:
            return APIResponse(code=status.HTTP_400_BAD_REQUEST, msg=f"审核失败， 原因：该任务是{task_object.status}状态，不允许审核")

    def calculate_user_points(self, user_id: str, points: float):
        balance_obj = self._dm.get_balance_object(user_id)
        balance_obj.total_points = round_2(Decimal(balance_obj.total_points) + Decimal(points))
        self.db.commit()
