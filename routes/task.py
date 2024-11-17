from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy.orm import Session
from models.request import AddTaskRequest, TaskListRequest, AuditTaskRequest, WorkerRecordRequest
from models.common import APIResponse, TokenData
from services.common import verify_user_request, get_db, get_task_service, get_storage_service
from utils.logger import LoguruLogger
from routes import auth

task_router = APIRouter(
    tags=["task"],
    include_in_schema=True
)


@task_router.post("/task/wechat/get_tasks")
def get_tasks(request: TaskListRequest, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat get_tasks..., params: {}".format(request.model_dump_json()))

    return get_task_service(db).get_task_list(request)


@task_router.get("/task/wechat/get_task")
def get_task_detail(task_id: str, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat get_tasks..., params - task_id: {}".format(task_id))
    return get_task_service(db).get_task(task_id)


@task_router.post("/task/wechat/add_task")
def add_task(request: AddTaskRequest, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat add_task...")
    logger.info(request)
    return get_task_service(db).add_task(request)


@task_router.post("/task/wechat/audit_task")
@auth.has_permission(["task:audit"])
def audit_task(request: AuditTaskRequest, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat audit task... params: {}".format(request.model_dump_json()))
    return get_task_service(db).audit_task_approval(request.task_id, request.approve_result, request.comment)


@task_router.post("/task/wechat/get_worker_record")
def get_worker_record(request: WorkerRecordRequest, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("get_all_worker...")
    return get_task_service(db).get_worker_record(request)
