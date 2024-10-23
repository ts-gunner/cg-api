from fastapi import APIRouter
from models.common import APIResponse
from utils.logger import LoguruLogger
import os

home_router = APIRouter(
    tags=["home"],
    include_in_schema=True
)


@home_router.get("/")
def root():
    logger = LoguruLogger.get_logger()
    logger.info("Welcome to the yami-api!!!")
    return APIResponse(msg="Welcome to the cg-api!!!")


@home_router.get("/appInfo")
def get_version():
    data = {
        "app_version": os.environ["APP_VERSION"]
    }
    return APIResponse(data=data)