from fastapi import APIRouter, UploadFile, Depends
from models.common import APIResponse, TokenData
from utils.logger import LoguruLogger
from services.common import verify_user_request, get_storage_service
import os

file_router = APIRouter(
    tags=["files"],
    include_in_schema=True
)


@file_router.post("/files/wechat/upload_attachment")
async def upload_file(blob: UploadFile, token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat save_task_attachment...")
    storage = get_storage_service()
    file_content = await blob.read()
    remote_url = storage.put_file(file_content, f"/{token_data.user_id}/{blob.filename}")
    return APIResponse(data=remote_url)
