from fastapi import APIRouter, Query
from utils.logger import LoguruLogger
from services.wechat import WeChatService

auth_router = APIRouter(
    tags=["auth"],
    include_in_schema=True
)


@auth_router.get("/auth/wechat/login")
def wechat_login(code: str):
    logger = LoguruLogger.get_logger()
    logger.info("wechat login...")
    res = WeChatService.we_login(code)
    logger.info("wechat login successfully!!")
    logger.info(res)
    return res
