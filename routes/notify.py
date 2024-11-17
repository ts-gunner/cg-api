from fastapi import APIRouter
from models.common import APIResponse
from utils.logger import LoguruLogger

notify_router = APIRouter(
    tags=["notify"],
    include_in_schema=True
)


@notify_router.get("/notify/get_notification")
def get_notification():
    logger = LoguruLogger.get_logger()
    logger.info("Welcome to the yami-api!!!")
    return APIResponse(msg="Welcome to the cg-api!!!")

